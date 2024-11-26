import pandas as pd
import os
from infoconnect.conf.index import TASK

file_name = f'out/data{TASK["TASK_CODE"]}.csv'
file_name_excel = f'out/data{TASK["TASK_CODE"]}.xlsx'
if os.path.exists(file_name):
    os.remove(file_name)


data_name = f'notice_{TASK["TASK_CODE"]}'
price_name = f'price_{TASK["TASK_CODE"]}'
contract_name = f'contract_{TASK["TASK_CODE"]}'

data_df = pd.read_csv(f'out/{data_name}.csv', sep=',')
price_df = pd.read_csv(f'out/{price_name}.csv', sep=',')
contract_df = pd.read_csv(f'out/{contract_name}.csv', sep=',')

source_list = data_df["网站链接"].tolist()
price_list = price_df["网站链接"].tolist()
price_value_list = price_df["最高限价"].tolist()

contract_list = contract_df["网站链接"].tolist()
contract_contractCode_list = contract_df["合同编号"].tolist()
contract_supplierContact_list = contract_df["供应商联系方式"].tolist()

result_list = []
result_contractCode_list = []
result_supplierContact_list = []

# 采购公告和结果一一对应
for i in range(len(source_list)):
    try:
        index = price_list.index(source_list[i])

        # 网站链接
        # print(f'link i: {i} source_list[i] {source_list[i]}')
        # 找到对应的合同数据

        # 合同和结果公告是 1 对 多
        c_index_list = []

        for item_index in range(len(contract_list)):
            if contract_list[item_index] == source_list[index]:
                c_index_list.append(item_index)

        # print(f'c_index_list: {c_index_list}')
        c_contractCode_list = []
        c_supplierContact_list = []
        for c_index in c_index_list:
            c_contractCode_list.append(
                contract_contractCode_list[c_index])
            c_supplierContact_list.append(
                contract_supplierContact_list[c_index])

        # print(f'c_supplierContact_list {",".join(c_supplierContact_list)} ')
        result_contractCode_list.append(",".join(c_contractCode_list))
        result_supplierContact_list.append(",".join(c_supplierContact_list))
        result_list.append(price_value_list[index])
    except ValueError:
        result_list.append('')
        result_supplierContact_list.append('')
        result_contractCode_list.append('')


# 字段顺序调整都需要改动这里
data_df.insert(12, "最高限价", result_list)
# data_df.insert(13, "合同编号", result_contractCode_list)
# data_df.insert(14, "供应商联系方式", result_supplierContact_list)

data_df.to_csv(file_name)
data_df.to_excel(file_name_excel)
