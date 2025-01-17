
class ShangHaiArea():
    def __init__(self):
        self.data = [
            {"value": "319900", "name": "上海市本级 "},
            {"value": "310101", "name": "黄浦区 "},
            {"value": "310104", "name": "徐汇区 "},
            {"value": "310105", "name": "长宁区 "},
            {"value": "310106", "name": "静安区 "},
            {"value": "310107", "name": "普陀区 "},
            {"value": "310109", "name": "虹口区 "},
            {"value": "310110", "name": "杨浦区 "},
            {"value": "310112", "name": "闵行区 "},
            {"value": "310113", "name": "宝山区 "},
            {"value": "310114", "name": "嘉定区 "},
            {"value": "310115", "name": "浦东新区 "},
            {"value": "310116", "name": "金山区 "},
            {"value": "310117", "name": "松江区 "},
            {"value": "310118", "name": "青浦区 "},
            {"value": "310120", "name": "奉贤区 "},
            {"value": "310151", "name": "崇明区 "},
        ]

    def export_province(self):
        return '上海市'

    def get_areainfo_by_value(self, target_value):
        result_area = {
            "province": self.export_province(),
            "county": '上海市',
            "district": ''
        }

        for item in self.data:
            if item["value"] == target_value:
                result_area["district"] = item["name"]

        return result_area
