from faker import Faker
from faker.providers import DynamicProvider
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, DECIMAL, DateTime

fake = Faker('zh_CN')

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

    def export_city(self, target_district):
        district_and_city = self.district_and_city_list()
        for item in district_and_city:
            [district, city] = item
            if (district == target_district):
                return city

    def export_province(self):
        return '浙江省'


area = Area()
area_district_list = area.export_district_list()

# # 地区
# area_district_provider = DynamicProvider(
#     provider_name="area_district",
#     elements=area_district_list
# )

# fake.add_provider(area_district_provider)

engine = create_engine(
    'mysql://infoconnect:noNaanKAlnX8h1mx@101.200.77.202/infoConnect')


dynamic_provider_list = [
    {
        'name': 'area_district',
        'list': area_district_list
    },
    {
        'name': 'school',
        'list': ["学校", "大学", "小学", "职业技术学院", "学院", "教育局", "教育集团", "职高"],
    },
    {
        'name': 'school_things',
        'list': ["教室",
                 "智慧教室",
                 "多媒体教室"
                 "实训室",
                 "专用教室",
                 "学科教室",
                 "阶梯教室",
                 "微格教室",
                 "创客教室",
                 "智慧计算机教室",
                 "中控",
                 "网络中控",
                 "中控主机",
                 "中央控制器",
                 "集中控制管理系统",
                 "控制面板",
                 "融合管理终端",
                 "智能集控管理终端",
                 "物联网控制中心",
                 "中央控制系统",
                 "讲台",
                 "讲桌",
                 "讨论桌",
                 "研讨桌",
                 "实训桌",
                 "演讲桌",
                 "演讲台",
                 "电子班牌",
                 "智能信息展示屏",
                 "智慧助教软件",
                 "智慧校园管理融合平台"
                 ],
    },
    {
        'name': 'model_things',
        'list': [
            ""
        ]
    },
    {
        'name': 'product_things',
        'list': [
            ""
        ]
    },
    {
        'name': 'brand_things',
        'list': [
            ""
        ]
    }

]

for dynamic_provider in dynamic_provider_list:
    provider_name = dynamic_provider["name"]
    provider_list = dynamic_provider["list"]

    provider = DynamicProvider(
        provider_name=provider_name,
        elements=provider_list
    )

    fake.add_provider(provider)


Q1_buyer_supplier_result_table_list = []
Q2_supplier_brand_projInfo_table_list = []

result_table_list = [
    {
        'table_name': 'Q1_buyer_supplier_result_table_fake',
        'list': Q1_buyer_supplier_result_table_list,
        #               项目编号	        notice_id	项目名称	区域_省	                区域_市	        区域_县区	采购人_名称	标项序号	合同编号	标项名称	预算金额	中标金额	供应商_名称（中标单位）	中标日期	url
        'columns': ['project_code', 'notice_id', 'project_name',  'area_province', 'area_city', 'area_district_or_county', 'purchaser_name', 'subject_no', 'contract_no', 'subject_name', 'budget_amount', 'bid_winning_amount', 'supplier_name', 'bid_winning_date'],
        'MAX_COUNT': 1000,
        "dtype": {"bid_winning_amount": DECIMAL(12, 2), "budget_amount": DECIMAL(12, 2), "bid_winning_date": DateTime}
    },
    {
        'table_name': 'Q2_supplier_brand_projInfo_table_fake',
        'list': Q2_supplier_brand_projInfo_table_list,
        # 供应商_名称（中标单位）	brand	product	model	quantity	unit_price	subtotal	                   项目编号	notice_id	    合同编号	    标项序号	    产品序号	区域_省	区域_市	区域_县区	中标日期
        'columns': ['supplier_name', 'brand', 'product',  'model', 'quantity', 'unit_price', 'subtotal', 'project_code', 'notice_id', 'contract_no', 'subject_no', 'product_no', 'area_province', 'area_city', 'area_district_or_county', 'bid_winning_date'],
        'MAX_COUNT': 1000,
        "dtype": {"bid_winning_date": DateTime}
    }]


for table in result_table_list:
    table_name = table["table_name"]
    list = table["list"]
    columns = table["columns"]
    MAX_COUNT = table["MAX_COUNT"]
    dtype = table["dtype"]

    for _ in range(MAX_COUNT):
        if table_name == 'Q1_buyer_supplier_result_table_fake':
            project_code = fake.sentence(nb_words=2, ext_word_list=['ABC', 'NBITC', 'JHCG', 'XHZFCG']).rstrip(".") + '-' + fake.date_between('-6y').strftime("%Y%m%d") + \
                '-' + str(np.random.randint(1, 243 + 1))
            notice_id = str(np.random.randint(
                1, 9216273 + 1))

            area_district_or_county = fake.area_district()
            area_city = area.export_city(area_district_or_county)
            area_province = area.export_province()

            project_name = area_city + area_district_or_county + fake.school_things() + \
                '采购项目'

            purchaser_name = area_city + area_district_or_county + fake.company_prefix() + \
                fake.school()
            subject_no = str(np.random.randint(
                1, 5 + 1))
            contract_no = '11N' + fake.ssn()
            subject_name = area_city + area_district_or_county + fake.school_things() + \
                '采购项目'
            budget_amount = str(np.random.randint(
                1, 6000000 + 1))
            bid_winning_amount = str(np.random.randint(
                1, 5800000 + 1))
            supplier_name = fake.company()
            bid_winning_date = fake.date_between('-6y').strftime("%Y-%m-%d")
            list.append((
                project_code,
                notice_id,
                project_name,
                area_province,
                area_city,
                area_district_or_county,
                purchaser_name,
                subject_no,
                contract_no,
                subject_name,
                budget_amount,
                bid_winning_amount,
                supplier_name,
                bid_winning_date,
            ))

        else:
            supplier_name = fake.company()
            brand = np.random.randint(
                1, 9216273 + 1)
            product = fake.product_things()
            model = fake.model_things()
            quantity = np.random.randint(
                1, 3000 + 1)
            unit_price = np.random.randint(
                1, 20000 + 1)
            subtotal = str(quantity * unit_price)
            project_code = fake.sentence(nb_words=2, ext_word_list=['ABC', 'NBITC', 'JHCG', 'XHZFCG']).rstrip(".") + '-' + fake.date_between('-6y').strftime("%Y%m%d") + \
                '-' + str(np.random.randint(1, 243 + 1))
            notice_id = str(np.random.randint(
                1, 9216273 + 1))
            contract_no = '11N' + fake.ssn()
            subject_no = str(np.random.randint(
                1, 5 + 1))
            product_no = fake.name()
            area_district_or_county = fake.area_district()
            area_city = area.export_city(area_district_or_county)
            area_province = area.export_province()

            bid_winning_date = fake.date_between('-6y').strftime("%Y-%m-%d")

            list.append((
                supplier_name,
                brand,
                product,
                model,
                quantity,
                unit_price,
                subtotal,
                project_code,
                notice_id,
                contract_no,
                subject_no,
                product_no,
                area_province,
                area_city,
                area_district_or_county,
                bid_winning_date,
            ))

    df = pd.DataFrame(data=np.array(list), columns=columns)

    print(df)
    print('================================================')
    df.to_sql(table_name, con=engine, if_exists='replace', dtype=dtype)
