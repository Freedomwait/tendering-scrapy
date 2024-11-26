import json
import requests

start_url = 'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results?pId=953&url=district'

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}


class Area():
    def __init__(self):

        res = requests.get(start_url, headers=Headers, stream=True)
        resJson = json.loads(res.content.decode('utf-8'))
        data = resJson["data"]

        list = []
        for item in data:
            out = {
                'value': item["name"],
                # 'id': item["id"],
                'label': item["name"],
                # 'code': item["code"],
            }

            item_url = f'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results?pId={item["id"]}&url=district'

            item_res = requests.get(item_url, headers=Headers, stream=True)
            item_res_json = json.loads(item_res.content.decode('utf-8'))

            out_children_list = []
            for inner_item in item_res_json["data"]:
                out_children_list.append({
                    "value": inner_item["name"],
                    "label": inner_item["name"],
                    # "id": inner_item["id"],
                    # 'code': inner_item["code"],
                })

            out["children"] = out_children_list

            list.append(out)
        print(list)
        self.data = list
        # self.data = [
        #     {"value": "339900", "id": "10065", "label": "浙江省本级", "children": []},
        #     {
        #         "value": "330100",
        #         "id": "954",
        #         "label": "杭州市",
        #         "children": [
        #             {"value": "330199", "label": "杭州市本级", "id": "10044"},
        #             {"value": "330102", "label": "上城区", "id": "955"},
        #             {"value": "330103", "label": "下城区", "id": "956"},
        #             {"value": "330104", "label": "江干区", "id": "957"},
        #             {"value": "330105", "label": "拱墅区", "id": "958"},
        #             {"value": "330106", "label": "西湖区", "id": "959"},
        #             {"value": "330108", "label": "滨江区", "id": "960"},
        #             {"value": "330109", "label": "萧山区", "id": "961"},
        #             {"value": "330110", "label": "余杭区", "id": "962"},
        #             {"value": "330113", "label": "临平工业园区", "id": "4021"},
        #             {"value": "330117", "label": "钱塘区", "id": "10040"},
        #             {"value": "330118", "label": "大江东区", "id": "10018"},
        #             {"value": "330122", "label": "桐庐县", "id": "963"},
        #             {"value": "330127", "label": "淳安县", "id": "964"},
        #             {"value": "330182", "label": "建德市", "id": "965"},
        #             {"value": "330183", "label": "富阳区", "id": "10043"},
        #             {"value": "330185", "label": "临安区", "id": "10051"},
        #             {"value": "330195", "label": "临平区", "id": "46401"},
        #             {"value": "330196", "label": "钱江开发区", "id": "4001"},
        #             {"value": "330197", "label": "西湖风景名胜区", "id": "10057"},
        #             {"value": "330198", "label": "杭州开发区", "id": "10050"}
        #         ]
        #     },
        #     {
        #         "value": "330200",
        #         "id": "968",
        #         "label": "宁波市",
        #         "children": [
        #             {"value": "330299", "label": "宁波市本级", "id": "4009"},
        #             {"value": "330203", "label": "海曙区", "id": "969"},
        #             {"value": "330205", "label": "江北区", "id": "971"},
        #             {"value": "330206", "label": "北仑区", "id": "972"},
        #             {"value": "330211", "label": "镇海区", "id": "973"},
        #             {"value": "330212", "label": "鄞州区", "id": "974"},
        #             {"value": "330225", "label": "象山县", "id": "975"},
        #             {"value": "330226", "label": "宁海县", "id": "976"},
        #             {"value": "330281", "label": "余姚市", "id": "977"},
        #             {"value": "330282", "label": "慈溪市", "id": "978"},
        #             {"value": "330283", "label": "奉化区", "id": "10061"},
        #             {"value": "330293", "label": "国家高新技术产业开发区", "id": "10030"},
        #             {"value": "330294", "label": "东钱湖区", "id": "4004"},
        #             {"value": "330295", "label": "前湾新区", "id": "4005"},
        #             {"value": "330296", "label": "保税区", "id": "10039"},
        #             {"value": "330297", "label": "大榭开发区", "id": "4007"},
        #             {"value": "330298", "label": "宁波开发区", "id": "4008"}
        #         ]
        #     },
        #     {
        #         "value": "330300",
        #         "id": "10027",
        #         "label": "温州市",
        #         "children": [
        #             {"value": "330399", "label": "温州市本级", "id": "4011"},
        #             {"value": "330302", "label": "鹿城区", "id": "981"},
        #             {"value": "330303", "label": "龙湾区", "id": "10020"},
        #             {"value": "330304", "label": "瓯海区", "id": "983"},
        #             {"value": "330316", "label": "温州开发区", "id": "10033"},
        #             {"value": "330317", "label": "瓯江口产业聚集区", "id": "10058"},
        #             {"value": "330318", "label": "温州生态园区", "id": "10072"},
        #             {"value": "330319", "label": "温州浙南科技城", "id": "10055"},
        #             {"value": "330322", "label": "洞头区", "id": "10002"},
        #             {"value": "330324", "label": "永嘉县", "id": "985"},
        #             {"value": "330326", "label": "平阳县", "id": "986"},
        #             {"value": "330327", "label": "苍南县", "id": "987"},
        #             {"value": "330328", "label": "文成县", "id": "988"},
        #             {"value": "330329", "label": "泰顺县", "id": "989"},
        #             {"value": "330381", "label": "瑞安市", "id": "990"},
        #             {"value": "330382", "label": "乐清市", "id": "991"},
        #             {"value": "330397", "label": "龙港市", "id": "43803"},
        #             {"value": "330398", "label": "温州开发区（老）", "id": "10031"}
        #         ]
        #     },
        #     {
        #         "value": "330400",
        #         "id": "992",
        #         "label": "嘉兴市",
        #         "children": [
        #             {"value": "330499", "label": "嘉兴市本级", "id": "4013"},
        #             {"value": "330402", "label": "南湖区", "id": "10053"},
        #             {"value": "330411", "label": "秀洲区", "id": "994"},
        #             {"value": "330420", "label": "嘉兴港区", "id": "10078"},
        #             {"value": "330421", "label": "嘉善县", "id": "995"},
        #             {"value": "330424", "label": "海盐县", "id": "996"},
        #             {"value": "330481", "label": "海宁市", "id": "997"},
        #             {"value": "330482", "label": "平湖市", "id": "998"},
        #             {"value": "330483", "label": "桐乡市", "id": "999"},
        #             {"value": "330498", "label": "嘉兴开发区", "id": "10004"}
        #         ]
        #     },
        #     {
        #         "value": "330500",
        #         "id": "1000",
        #         "label": "湖州市",
        #         "children": [
        #             {"value": "330599", "label": "湖州市本级", "id": "4025"},
        #             {"value": "330502", "label": "吴兴区", "id": "1001"},
        #             {"value": "330503", "label": "南浔区", "id": "1002"},
        #             {"value": "330518", "label": "湖州度假区", "id": "10071"},
        #             {"value": "330521", "label": "德清县", "id": "1003"},
        #             {"value": "330522", "label": "长兴县", "id": "1004"},
        #             {"value": "330523", "label": "安吉县", "id": "1005"},
        #             {"value": "330590", "label": "南太湖新区", "id": "42201"},
        #             {"value": "330598", "label": "湖州开发区", "id": "4014"}
        #         ]
        #     },
        #     {
        #         "value": "330600",
        #         "id": "1006",
        #         "label": "绍兴市",
        #         "children": [
        #             {"value": "330699", "label": "绍兴市本级", "id": "4015"},
        #             {"value": "330602", "label": "越城区", "id": "1007"},
        #             {"value": "330603", "label": "柯桥区", "id": "10069"},
        #             {"value": "330618", "label": "滨海区", "id": "10074"},
        #             {"value": "330624", "label": "新昌县", "id": "1009"},
        #             {"value": "330681", "label": "诸暨市", "id": "1010"},
        #             {"value": "330682", "label": "上虞区", "id": "10017"},
        #             {"value": "330683", "label": "嵊州市", "id": "1012"}
        #         ]
        #     },
        #     {
        #         "value": "330700",
        #         "id": "1013",
        #         "label": "金华市",
        #         "children": [
        #             {"value": "330799", "label": "金华市本级", "id": "4017"},
        #             {"value": "330702", "label": "婺城区", "id": "1014"},
        #             {"value": "330703", "label": "金东区", "id": "1015"},
        #             {"value": "330716", "label": "金义都市新区", "id": "10005"},
        #             {"value": "330717", "label": "金华山", "id": "10062"},
        #             {"value": "330723", "label": "武义县", "id": "1016"},
        #             {"value": "330726", "label": "浦江县", "id": "1017"},
        #             {"value": "330727", "label": "磐安县", "id": "1018"},
        #             {"value": "330781", "label": "兰溪市", "id": "1019"},
        #             {"value": "330782", "label": "义乌市", "id": "1020"},
        #             {"value": "330783", "label": "东阳市", "id": "1021"},
        #             {"value": "330784", "label": "永康市", "id": "1022"},
        #             {"value": "330798", "label": "金华开发区", "id": "4016"}
        #         ]
        #     },
        #     {
        #         "value": "330800",
        #         "id": "1023",
        #         "label": "衢州市",
        #         "children": [
        #             {"value": "330899", "label": "衢州市本级", "id": "4018"},
        #             {"value": "330802", "label": "柯城区", "id": "1024"},
        #             {"value": "330803", "label": "衢江区", "id": "1025"},
        #             {"value": "330822", "label": "常山县", "id": "1026"},
        #             {"value": "330824", "label": "开化县", "id": "1027"},
        #             {"value": "330825", "label": "龙游县", "id": "1028"},
        #             {"value": "330881", "label": "江山市", "id": "1029"},
        #             {"value": "330882", "label": "衢州绿色产业区", "id": "10025"}
        #         ]
        #     },
        #     {
        #         "value": "330900",
        #         "id": "1030",
        #         "label": "舟山市",
        #         "children": [
        #             {"value": "330999", "label": "舟山市本级", "id": "4019"},
        #             {"value": "330902", "label": "定海区", "id": "1031"},
        #             {"value": "330903", "label": "普陀区", "id": "1032"},
        #             {"value": "330921", "label": "岱山县", "id": "1033"},
        #             {"value": "330922", "label": "嵊泗县", "id": "1034"},
        #             {"value": "330950", "label": "高新区管委会", "id": "10046"},
        #             {
        #                 "value": "330951",
        #                 "label": "舟山群岛新区普陀山－朱家尖管理委员会",
        #                 "id": "10007"
        #             },
        #             {
        #                 "value": "330952",
        #                 "label": "舟山群岛新区新城管理委员会",
        #                 "id": "10073"
        #             }
        #         ]
        #     },
        #     {
        #         "value": "331000",
        #         "id": "1035",
        #         "label": "台州市",
        #         "children": [
        #             {"value": "331099", "label": "台州市本级", "id": "10047"},
        #             {"value": "331002", "label": "椒江区", "id": "1036"},
        #             {"value": "331003", "label": "黄岩区", "id": "1037"},
        #             {"value": "331004", "label": "路桥区", "id": "1038"},
        #             {"value": "331021", "label": "玉环市", "id": "1039"},
        #             {"value": "331022", "label": "三门县", "id": "1040"},
        #             {"value": "331023", "label": "天台县", "id": "1041"},
        #             {"value": "331024", "label": "仙居县", "id": "1042"},
        #             {"value": "331081", "label": "温岭市", "id": "1043"},
        #             {"value": "331082", "label": "临海市", "id": "1044"}
        #         ]
        #     },
        #     {
        #         "value": "331100",
        #         "id": "1045",
        #         "label": "丽水市",
        #         "children": [
        #             {"value": "331199", "label": "丽水市本级", "id": "4026"},
        #             {"value": "331102", "label": "莲都区", "id": "1046"},
        #             {"value": "331103", "label": "丽水开发区", "id": "10024"},
        #             {"value": "331121", "label": "青田县", "id": "1047"},
        #             {"value": "331122", "label": "缙云县", "id": "1048"},
        #             {"value": "331123", "label": "遂昌县", "id": "1049"},
        #             {"value": "331124", "label": "松阳县", "id": "1050"},
        #             {"value": "331125", "label": "云和县", "id": "1051"},
        #             {"value": "331126", "label": "庆元县", "id": "1052"},
        #             {"value": "331127", "label": "景宁畲族自治县", "id": "1053"},
        #             {"value": "331181", "label": "龙泉市", "id": "1054"}
        #         ]
        #     }
        # ]

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

    def export_province():
        return '浙江省'


area = Area()
print(area.export_json_tree())
