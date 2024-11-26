import pandas as pd
from urllib.parse import urlparse, parse_qs


task_code = '2023_1_4_1'
output_dir = 'input/D1_table'

# data_df = pd.read_csv(
#     'input/structured_raw_selected_xiulan.csv')

# 从文件中提取所有的内容，分成四个表
notice_data_df = pd.read_csv(f'out/notice_{task_code}.csv')
purchase_data_df = pd.read_csv(f'out/price_{task_code}.csv')
contract_data_df = pd.read_csv(f'out/contract_{task_code}.csv')


def get_noticeid_by_url(url):
    return parse_qs(urlparse(url).query)[
        'noticeId'][0]


area_tree_data = [
    {"value": "339900", "id": "10065", "label": "浙江省本级", "children": []},
    {
        "value": "330100",
        "id": "954",
        "label": "杭州市",
        "children": [
            {"value": "330199", "label": "杭州市本级", "id": "10044"},
            {"value": "330102", "label": "上城区", "id": "955"},
            {"value": "330103", "label": "下城区", "id": "956"},
            {"value": "330104", "label": "江干区", "id": "957"},
            {"value": "330105", "label": "拱墅区", "id": "958"},
            {"value": "330106", "label": "西湖区", "id": "959"},
            {"value": "330108", "label": "滨江区", "id": "960"},
            {"value": "330109", "label": "萧山区", "id": "961"},
            {"value": "330110", "label": "余杭区", "id": "962"},
            {"value": "330113", "label": "临平工业园区", "id": "4021"},
            {"value": "330117", "label": "钱塘区", "id": "10040"},
            {"value": "330118", "label": "大江东区", "id": "10018"},
            {"value": "330122", "label": "桐庐县", "id": "963"},
            {"value": "330127", "label": "淳安县", "id": "964"},
            {"value": "330182", "label": "建德市", "id": "965"},
            {"value": "330183", "label": "富阳区", "id": "10043"},
            {"value": "330185", "label": "临安区", "id": "10051"},
            {"value": "330195", "label": "临平区", "id": "46401"},
            {"value": "330196", "label": "钱江开发区", "id": "4001"},
            {"value": "330197", "label": "西湖风景名胜区", "id": "10057"},
            {"value": "330198", "label": "杭州开发区", "id": "10050"}
        ]
    },
    {
        "value": "330200",
        "id": "968",
        "label": "宁波市",
        "children": [
            {"value": "330299", "label": "宁波市本级", "id": "4009"},
            {"value": "330203", "label": "海曙区", "id": "969"},
            {"value": "330205", "label": "江北区", "id": "971"},
            {"value": "330206", "label": "北仑区", "id": "972"},
            {"value": "330211", "label": "镇海区", "id": "973"},
            {"value": "330212", "label": "鄞州区", "id": "974"},
            {"value": "330225", "label": "象山县", "id": "975"},
            {"value": "330226", "label": "宁海县", "id": "976"},
            {"value": "330281", "label": "余姚市", "id": "977"},
            {"value": "330282", "label": "慈溪市", "id": "978"},
            {"value": "330283", "label": "奉化区", "id": "10061"},
            {"value": "330293", "label": "国家高新技术产业开发区", "id": "10030"},
            {"value": "330294", "label": "东钱湖区", "id": "4004"},
            {"value": "330295", "label": "前湾新区", "id": "4005"},
            {"value": "330296", "label": "保税区", "id": "10039"},
            {"value": "330297", "label": "大榭开发区", "id": "4007"},
            {"value": "330298", "label": "宁波开发区", "id": "4008"}
        ]
    },
    {
        "value": "330300",
        "id": "10027",
        "label": "温州市",
        "children": [
            {"value": "330399", "label": "温州市本级", "id": "4011"},
            {"value": "330302", "label": "鹿城区", "id": "981"},
            {"value": "330303", "label": "龙湾区", "id": "10020"},
            {"value": "330304", "label": "瓯海区", "id": "983"},
            {"value": "330316", "label": "温州开发区", "id": "10033"},
            {"value": "330317", "label": "瓯江口产业聚集区", "id": "10058"},
            {"value": "330318", "label": "温州生态园区", "id": "10072"},
            {"value": "330319", "label": "温州浙南科技城", "id": "10055"},
            {"value": "330322", "label": "洞头区", "id": "10002"},
            {"value": "330324", "label": "永嘉县", "id": "985"},
            {"value": "330326", "label": "平阳县", "id": "986"},
            {"value": "330327", "label": "苍南县", "id": "987"},
            {"value": "330328", "label": "文成县", "id": "988"},
            {"value": "330329", "label": "泰顺县", "id": "989"},
            {"value": "330381", "label": "瑞安市", "id": "990"},
            {"value": "330382", "label": "乐清市", "id": "991"},
            {"value": "330397", "label": "龙港市", "id": "43803"},
            {"value": "330398", "label": "温州开发区（老）", "id": "10031"}
        ]
    },
    {
        "value": "330400",
        "id": "992",
        "label": "嘉兴市",
        "children": [
            {"value": "330499", "label": "嘉兴市本级", "id": "4013"},
            {"value": "330402", "label": "南湖区", "id": "10053"},
            {"value": "330411", "label": "秀洲区", "id": "994"},
            {"value": "330420", "label": "嘉兴港区", "id": "10078"},
            {"value": "330421", "label": "嘉善县", "id": "995"},
            {"value": "330424", "label": "海盐县", "id": "996"},
            {"value": "330481", "label": "海宁市", "id": "997"},
            {"value": "330482", "label": "平湖市", "id": "998"},
            {"value": "330483", "label": "桐乡市", "id": "999"},
            {"value": "330498", "label": "嘉兴开发区", "id": "10004"}
        ]
    },
    {
        "value": "330500",
        "id": "1000",
        "label": "湖州市",
        "children": [
            {"value": "330599", "label": "湖州市本级", "id": "4025"},
            {"value": "330502", "label": "吴兴区", "id": "1001"},
            {"value": "330503", "label": "南浔区", "id": "1002"},
            {"value": "330518", "label": "湖州度假区", "id": "10071"},
            {"value": "330521", "label": "德清县", "id": "1003"},
            {"value": "330522", "label": "长兴县", "id": "1004"},
            {"value": "330523", "label": "安吉县", "id": "1005"},
            {"value": "330590", "label": "南太湖新区", "id": "42201"},
            {"value": "330598", "label": "湖州开发区", "id": "4014"}
        ]
    },
    {
        "value": "330600",
        "id": "1006",
        "label": "绍兴市",
        "children": [
            {"value": "330699", "label": "绍兴市本级", "id": "4015"},
            {"value": "330602", "label": "越城区", "id": "1007"},
            {"value": "330603", "label": "柯桥区", "id": "10069"},
            {"value": "330618", "label": "滨海区", "id": "10074"},
            {"value": "330624", "label": "新昌县", "id": "1009"},
            {"value": "330681", "label": "诸暨市", "id": "1010"},
            {"value": "330682", "label": "上虞区", "id": "10017"},
            {"value": "330683", "label": "嵊州市", "id": "1012"}
        ]
    },
    {
        "value": "330700",
        "id": "1013",
        "label": "金华市",
        "children": [
            {"value": "330799", "label": "金华市本级", "id": "4017"},
            {"value": "330702", "label": "婺城区", "id": "1014"},
            {"value": "330703", "label": "金东区", "id": "1015"},
            {"value": "330716", "label": "金义都市新区", "id": "10005"},
            {"value": "330717", "label": "金华山", "id": "10062"},
            {"value": "330723", "label": "武义县", "id": "1016"},
            {"value": "330726", "label": "浦江县", "id": "1017"},
            {"value": "330727", "label": "磐安县", "id": "1018"},
            {"value": "330781", "label": "兰溪市", "id": "1019"},
            {"value": "330782", "label": "义乌市", "id": "1020"},
            {"value": "330783", "label": "东阳市", "id": "1021"},
            {"value": "330784", "label": "永康市", "id": "1022"},
            {"value": "330798", "label": "金华开发区", "id": "4016"}
        ]
    },
    {
        "value": "330800",
        "id": "1023",
        "label": "衢州市",
        "children": [
            {"value": "330899", "label": "衢州市本级", "id": "4018"},
            {"value": "330802", "label": "柯城区", "id": "1024"},
            {"value": "330803", "label": "衢江区", "id": "1025"},
            {"value": "330822", "label": "常山县", "id": "1026"},
            {"value": "330824", "label": "开化县", "id": "1027"},
            {"value": "330825", "label": "龙游县", "id": "1028"},
            {"value": "330881", "label": "江山市", "id": "1029"},
            {"value": "330882", "label": "衢州绿色产业区", "id": "10025"}
        ]
    },
    {
        "value": "330900",
        "id": "1030",
        "label": "舟山市",
        "children": [
            {"value": "330999", "label": "舟山市本级", "id": "4019"},
            {"value": "330902", "label": "定海区", "id": "1031"},
            {"value": "330903", "label": "普陀区", "id": "1032"},
            {"value": "330921", "label": "岱山县", "id": "1033"},
            {"value": "330922", "label": "嵊泗县", "id": "1034"},
            {"value": "330950", "label": "高新区管委会", "id": "10046"},
            {
                "value": "330951",
                "label": "舟山群岛新区普陀山－朱家尖管理委员会",
                "id": "10007"
            },
            {
                "value": "330952",
                "label": "舟山群岛新区新城管理委员会",
                "id": "10073"
            }
        ]
    },
    {
        "value": "331000",
        "id": "1035",
        "label": "台州市",
        "children": [
            {"value": "331099", "label": "台州市本级", "id": "10047"},
            {"value": "331002", "label": "椒江区", "id": "1036"},
            {"value": "331003", "label": "黄岩区", "id": "1037"},
            {"value": "331004", "label": "路桥区", "id": "1038"},
            {"value": "331021", "label": "玉环市", "id": "1039"},
            {"value": "331022", "label": "三门县", "id": "1040"},
            {"value": "331023", "label": "天台县", "id": "1041"},
            {"value": "331024", "label": "仙居县", "id": "1042"},
            {"value": "331081", "label": "温岭市", "id": "1043"},
            {"value": "331082", "label": "临海市", "id": "1044"}
        ]
    },
    {
        "value": "331100",
        "id": "1045",
        "label": "丽水市",
        "children": [
            {"value": "331199", "label": "丽水市本级", "id": "4026"},
            {"value": "331102", "label": "莲都区", "id": "1046"},
            {"value": "331103", "label": "丽水开发区", "id": "10024"},
            {"value": "331121", "label": "青田县", "id": "1047"},
            {"value": "331122", "label": "缙云县", "id": "1048"},
            {"value": "331123", "label": "遂昌县", "id": "1049"},
            {"value": "331124", "label": "松阳县", "id": "1050"},
            {"value": "331125", "label": "云和县", "id": "1051"},
            {"value": "331126", "label": "庆元县", "id": "1052"},
            {"value": "331127", "label": "景宁畲族自治县", "id": "1053"},
            {"value": "331181", "label": "龙泉市", "id": "1054"}
        ]
    }
]


class Area():
    def __init__(self):
        self.data = area_tree_data

    def export_json_tree(self):
        return self.data

    def district_and_city_list(self):
        result = []
        for item in self.data:
            children = item['children']
            for child in children:
                result.append((child["label"], item["label"]))

        return result

    def export_district_list(self):
        district_and_city = self.district_and_city_list()
        list = []
        for item in district_and_city:
            [district, city] = item
            list.append(district)
        return list

    def export_city_list(self):
        district_and_city = self.district_and_city_list()
        list = []
        for item in district_and_city:
            [district, city] = item
            list.append(city)
        return list

    def export_city(self, target_district):
        district_and_city = self.district_and_city_list()
        for item in district_and_city:
            [district, city] = item
            if (district == target_district):
                return city

    def export_province(self):
        return '浙江省'


def are_item(dis):
    # 地区，拿地区反向查询 省市区

    area = Area()
    area_district_list = area.export_district_list()
    area_city_list = area.export_city_list()
    city = ''
    district = ''

    if dis in area_district_list:
        city = area.export_city(dis)
        district = dis
    elif dis in area_city_list:
        city = dis
        district = ''

    return {
        'pro': area.export_province(),
        'city': city,
        'dis': district
    }


url_list = notice_data_df["网站链接"].tolist()

# 所有结果公告ID
notice_id_list = []
project_code_list = []
project_name_list = []
project_type_list = []
area_pro_list = []
area_city_list = []
area_dis_list = []
purchase_name_list = []
purchaser_contract_list = []
purchaser_contract_phone_list = []
agent_name_list = []
agent_contract_list = []
agent_contract_phone_list = []
keyword_list = []

purchase_time_list = []
bid_winning_time_list = []
maximum_price_list = []
purchase_dead_line_list = []
request_url_list = []
project_count_list = []


def get_value_by_col_name(df_item, col_name):
    list = df_item.get(col_name).tolist()
    return list[0] if len(list) else ''


def build_url_noticeid(noticeId):
    return 'https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html?noticeId=' + str(noticeId)


for url in url_list:
    # 结果和采购 1-1 这里一起处理

    # 结果相关
    current_row = notice_data_df.loc[notice_data_df['网站链接'] == url]

    notice_id_list.append(get_noticeid_by_url(
        get_value_by_col_name(current_row, '网站链接')))
    project_code_list.append(get_value_by_col_name(current_row, '项目编号'))
    project_name_list.append(get_value_by_col_name(current_row, '项目名称'))

    dis = get_value_by_col_name(current_row, '地区')
    area = are_item(dis)
    area_pro_list.append(area["pro"])
    area_city_list.append(area["city"])
    area_dis_list.append(area["dis"])

    purchase_name_list.append(get_value_by_col_name(current_row, '采购人名称'))
    purchaser_contract_list.append(
        get_value_by_col_name(current_row, '采购项目联系人'))
    purchaser_contract_phone_list.append(
        get_value_by_col_name(current_row, '采购项目联系人联系方式'))
    agent_name_list.append(
        get_value_by_col_name(current_row, '招标代理名称'))
    agent_contract_list.append(
        get_value_by_col_name(current_row, '采购代理机构_项目联系人'))
    agent_contract_phone_list.append(
        get_value_by_col_name(current_row, '采购代理机构_项目联系方式'))
    keyword_list.append(
        get_value_by_col_name(current_row, '查询关键词'))

    purchase_time_list.append(get_value_by_col_name(current_row, '招标时间'))
    bid_winning_time_list.append(get_value_by_col_name(current_row, '中标时间'))

    # 采购相关项
    purchase_data_row = purchase_data_df.loc[purchase_data_df['网站链接'] == url]

    max_price = get_value_by_col_name(purchase_data_row, '最高限价')
    purchase_dead_line = get_value_by_col_name(purchase_data_row, '采购截止时间')
    purchase_type = get_value_by_col_name(purchase_data_row, '招采类型')

    # 最高限价有几个价格就是有几项
    project_count_list.append(len(max_price.split(",")))

    purchase_notice_id = str(get_value_by_col_name(
        purchase_data_row, '采购noticeId'))
    request_url = build_url_noticeid(
        purchase_notice_id if len(purchase_notice_id) else '')

    maximum_price_list.append(max_price)
    purchase_dead_line_list.append(purchase_dead_line)
    project_type_list.append(purchase_type)
    request_url_list.append(request_url)

default_list = []
for item in range(len(notice_id_list)):
    default_list.append('')


project_table_df = pd.DataFrame({
    "项目编号": project_code_list,
    "notice_id": notice_id_list,
    "项目名称": project_name_list,
    "招采类型": project_type_list,
    "区域_省": area_pro_list,
    "区域_市": area_city_list,
    "区域_县区": area_dis_list,
    "采购人_名称": purchase_name_list,
    "采购人_项目联系人": purchaser_contract_list,
    "采购人_项目联系方式": purchaser_contract_phone_list,
    "采购代理机构_名称": agent_name_list,
    "采购代理机构_项目联系人": agent_contract_list,
    "采购代理机构_项目联系方式": agent_contract_phone_list,
    "关键词": keyword_list
})

project_table_df.to_csv(f'{output_dir}/project_table.csv', index=False)


request_notice_table_df = pd.DataFrame({
    "项目编号": project_code_list,
    "notice_id": notice_id_list,
    "采购日期": purchase_time_list,
    "截止日期": purchase_dead_line_list,
    "预算金额": maximum_price_list,
    "标项_count": project_count_list,
    "URL": request_url_list,
})

# 清除没有采购公告的数据
request_notice_table_clean_df = request_notice_table_df.dropna(axis=0, subset=[
                                                               '采购日期'], how='any')

request_notice_table_clean_df.to_csv(
    f'{output_dir}/request_notice_table.csv', index=False)

result_notice_table_df = pd.DataFrame({
    "项目编号": project_code_list,
    "notice_id": notice_id_list,
    "中标日期": bid_winning_time_list,
    "URL": url_list,
})

result_notice_table_df.to_csv(
    f'{output_dir}/result_notice_table.csv', index=False)


# 采购公告按照标项进行拆分
web_url_list = []
count_list = []
name_list = []
max_price_list = []
for index, row in purchase_data_df.iterrows():
    if pd.isna(row["标项序号"]):
        pass
    else:
        project_name_list = row["标项名称"].split(",")
        for project_index in range(len(project_name_list)):
            web_url_list.append(row["网站链接"])
            count_list.append(str(project_index+1))
            name_list.append(project_name_list[project_index])
            max_price_list.append(row["最高限价"])

purchase_order_table_df = pd.DataFrame({
    "网站链接": web_url_list,
    "标项序号": count_list,
    "标项名称": name_list,
    "预算金额": max_price_list
})

# project_order_table_df.to_csv('test.csv')

# 结果和合同一对多，分开处理

m1_df = purchase_order_table_df.merge(notice_data_df, on="网站链接", how="right")

# 选中需要的列，并且清除为空的数据
selected_df = pd.DataFrame(
    m1_df, columns=['项目编号', '网站链接', '标项序号', '标项名称', '预算金额', '中标金额', '中标单位', '采购项目联系人']).dropna(axis=0, subset=[
        '标项序号'], how='any')

# 合并合同数据，但是这里直接 merge 会有问题，理论上一个标项对应一个合同信息
# m2_df = selected_df.merge(contract_data_df, how="right", on="网站链接")

selected_df.to_csv('selected_df.csv')


contract_project_code_list = []
contract_notice_id_list = []
contract_budget_account_list = []
contract_bid_winning_amount_list = []
contract_supplier_list = []
contract_project_person_list = []
contract_item_order_list = []
contract_item_name_list = []

# 合同编号, 供应商_合同联系方式, 标项合同url
contract_code_list = []
contract_supplier_phone_list = []
contract_url_list = []
# contract_web_url_list = []

for index, row in selected_df.iterrows():
    web_url = row["网站链接"]
    # if web_url == 'https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html?noticeId=8514386':
    # print(web_url)
    # contract_web_url_list.append(web_url)
    contract_notice_id_list.append(get_noticeid_by_url(web_url))
    contract_project_code_list.append(row["项目编号"])
    contract_budget_account_list.append(row["预算金额"])
    contract_bid_winning_amount_list.append(row["中标金额"])
    contract_supplier_list.append(row["中标单位"])
    contract_project_person_list.append(row["采购项目联系人"])
    contract_item_order_list.append(row["标项序号"])
    contract_item_name_list.append(row["标项名称"])
    current_contract_rows = contract_data_df.loc[contract_data_df['网站链接'] == web_url]
    matched_contract_rows = current_contract_rows["合同编号"].tolist()
    matched_phone_rows = current_contract_rows["供应商联系方式"].tolist()
    matched_id_rows = current_contract_rows["合同noticeId"].tolist()
    if len(matched_contract_rows):
        project_count_index = int(row["标项序号"])
        # 存在标项和合同数不对应的情况，这里取第一个
        # 可能存在废标
        if project_count_index <= len(matched_contract_rows):

            contract_code_list.append(
                matched_contract_rows[project_count_index - 1])

            contract_supplier_phone_list.append(
                matched_phone_rows[project_count_index - 1])
            contract_url_list.append(
                build_url_noticeid(matched_id_rows[project_count_index - 1]))
        else:
            print(f"web_url: {web_url} 标项和合同数不一致，可能存在废标或者其他数据异常")
            contract_code_list.append(matched_contract_rows[0])
            contract_supplier_phone_list.append(matched_phone_rows[0])
            contract_url_list.append(build_url_noticeid(matched_id_rows[0]))

    else:
        contract_code_list.append('')
        contract_supplier_phone_list.append('')
        contract_url_list.append('')

project_order_table_df = pd.DataFrame({
    "项目编号": contract_project_code_list,
    "notice_id": contract_notice_id_list,
    "标项序号": contract_item_order_list,
    "标项名称": contract_item_name_list,
    # "网站链接": contract_web_url_list,
    "预算金额": contract_budget_account_list,
    "中标金额": contract_bid_winning_amount_list,
    "供应商_名称（中标单位）": contract_supplier_list,
    "采购人_项目联系人": contract_project_person_list,
    "合同编号":  contract_code_list,
    "供应商联系方式": contract_supplier_phone_list,
    "标项合同url": contract_url_list
}).dropna(axis=0, subset=[
    '合同编号'], how='any')

project_order_table_df.to_csv(
    f'{output_dir}/project_order_table.csv', index=False)


# 这种合并方式会造成 多对多的交叉生成
# m3_df = selected_df.merge(m2_df, how="right", on="网站链接").drop_duplicates(
#     subset=None, keep="first", inplace=False)

# m3_df.to_csv('m3_df.csv')
