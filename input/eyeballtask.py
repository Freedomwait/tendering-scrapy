import pandas as pd
from urllib.parse import urlparse, parse_qs

task_code = '2022_12_12_1'

data_df = pd.read_csv(
    './structured_raw_selected_xiulan.csv')


def get_noticeid_by_url(url):
    return parse_qs(urlparse(url).query)[
        'noticeId'][0]


data = data_df["网站链接"].tolist()

# 所有结果公告ID
notice_id_list = []
for item in data:
    notice_id_list.append(get_noticeid_by_url(item))


print(notice_id_list)

# 关联数组
related_contract_list = []

file = open(
    f'../sql/related_contract_announcement{task_code}.txt', "r")
fileLines = file.readlines()

contract_id_list = []

for item in fileLines:
    # 因为合同存在多个，这里用 [] 来定位
    left_index = item.find("[")
    right_index = item.find("]")

    notice_id = item[:left_index - 1]

    # 多个合同公告
    contract_ids = item[left_index + 1:right_index]

    # 过滤空值
    if (len(contract_ids)):
        # 从文本中读出来的是 str 而不是 list
        contract_ids_list = contract_ids.replace(
            "'", '').replace(" '", '').split(",")
        for contract_id in contract_ids_list:

            if notice_id in notice_id_list:
                contract_id_list.append(contract_id)


file.close()
print(f'contract_id: {contract_id_list}')
