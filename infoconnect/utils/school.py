
class School:
    def __init__(self, text):
        self.text = text;
        self.SCHOOL_LIST = [
            {"code": "4133010335", "name": "浙江大学", "level": "本科"},
            {"code": "4133010336", "name": "杭州电子科技大学", "level": "本科"},
            {"code": "4133010337", "name": "浙江工业大学", "level": "本科"},
            {"code": "4133010338", "name": "浙江理工大学", "level": "本科"},
            {"code": "4133010340", "name": "浙江海洋大学", "level": "本科"},
            {"code": "4133010341", "name": "浙江农林大学", "level": "本科"},
            {"code": "4133010343", "name": "温州医科大学", "level": "本科"},
            {"code": "4133010344", "name": "浙江中医药大学", "level": "本科"},
            {"code": "4133010345", "name": "浙江师范大学", "level": "本科"},
            {"code": "4133010346", "name": "杭州师范大学", "level": "本科"},
            {"code": "4133010347", "name": "湖州师范学院", "level": "本科"},
            {"code": "4133010349", "name": "绍兴文理学院", "level": "本科"},
            {"code": "4133010350", "name": "台州学院", "level": "本科"},
            {"code": "4133010351", "name": "温州大学", "level": "本科"},
            {"code": "4133010352", "name": "丽水学院", "level": "本科"},
            {"code": "4133010353", "name": "浙江工商大学", "level": "本科"},
            {"code": "4133010354", "name": "嘉兴学院", "level": "本科"},
            {"code": "4133010355", "name": "中国美术学院", "level": "本科"},
            {"code": "4133010356", "name": "中国计量大学", "level": "本科"},
            {"code": "4133010876", "name": "浙江万里学院", "level": "本科"},
            {"code": "4133011057", "name": "浙江科技学院", "level": "本科"},
            {"code": "4133011058", "name": "宁波工程学院", "level": "本科"},
            {"code": "4133011481", "name": "浙江水利水电学院", "level": "本科"},
            {"code": "4133011482", "name": "浙江财经大学", "level": "本科"},
            {"code": "4133011483", "name": "浙江警察学院", "level": "本科"},
            {"code": "4133011488", "name": "衢州学院", "level": "本科"},
            {"code": "4133011646", "name": "宁波大学", "level": "本科"},
            {"code": "4133011647", "name": "浙江传媒学院", "level": "本科"},
            {"code": "4133011842", "name": "浙江树人学院", "level": "本科"},
            {"code": "4133012792", "name": "浙江越秀外国语学院", "level": "本科"},
            {"code": "4133013001", "name": "宁波财经学院", "level": "本科"},
            {"code": "4133013021", "name": "浙江大学城市学院", "level": "本科"},
            {"code": "4133013022", "name": "浙江大学宁波理工学院", "level": "本科"},
            {"code": "4133013023", "name": "杭州医学院", "level": "本科"},
            {"code": "4133013275", "name": "浙江工业大学之江学院", "level": "本科"},
            {"code": "4133013276", "name": "浙江师范大学行知学院", "level": "本科"},
            {"code": "4133013277", "name": "宁波大学科学技术学院", "level": "本科"},
            {
                "code": "4133013279",
                "name": "杭州电子科技大学信息工程学院",
                "level": "本科"
            },
            {
                "code": "4133013280",
                "name": "浙江理工大学科技与艺术学院",
                "level": "本科"
            },
            {
                "code": "4133013282",
                "name": "浙江海洋大学东海科学技术学院",
                "level": "本科"
            },
            {"code": "4133013283", "name": "浙江农林大学暨阳学院", "level": "本科"},
            {"code": "4133013284", "name": "温州医科大学仁济学院", "level": "本科"},
            {"code": "4133013285", "name": "浙江中医药大学滨江学院", "level": "本科"},
            {"code": "4133013286", "name": "杭州师范大学钱江学院", "level": "本科"},
            {"code": "4133013287", "name": "湖州师范学院求真学院", "level": "本科"},
            {"code": "4133013288", "name": "绍兴文理学院元培学院", "level": "本科"},
            {"code": "4133013289", "name": "温州大学瓯江学院", "level": "本科"},
            {"code": "4133013290", "name": "浙江工商大学杭州商学院", "level": "本科"},
            {"code": "4133013291", "name": "嘉兴学院南湖学院", "level": "本科"},
            {"code": "4133013292", "name": "中国计量大学现代科技学院", "level": "本科"},
            {"code": "4133013294", "name": "浙江财经大学东方学院", "level": "本科"},
            {"code": "4133013637", "name": "温州商学院", "level": "本科"},
            {"code": "4133014206", "name": "同济大学浙江学院", "level": "本科"},
            {"code": "4133014207", "name": "上海财经大学浙江学院", "level": "本科"},
            {"code": "4133014275", "name": "浙江外国语学院", "level": "本科"},
            {"code": "4133014535", "name": "浙江音乐学院", "level": "本科"},
            {"code": "4133014626", "name": "西湖大学", "level": "本科"},
            {"code": "4133016301", "name": "宁波诺丁汉大学", "level": "本科"},
            {"code": "4133016405", "name": "温州肯恩大学", "level": "本科"},
            {"code": "4133010863", "name": "宁波职业技术学院", "level": "专科"},
            {"code": "4133010864", "name": "温州职业技术学院", "level": "专科"},
            {"code": "4133012036", "name": "浙江交通职业技术学院", "level": "专科"},
            {"code": "4133012061", "name": "金华职业技术学院", "level": "专科"},
            {"code": "4133012645", "name": "宁波城市职业技术学院", "level": "专科"},
            {"code": "4133012646", "name": "浙江电力职业技术学院", "level": "专科"},
            {"code": "4133012647", "name": "浙江同济科技职业学院", "level": "专科"},
            {"code": "4133012789", "name": "浙江工商职业技术学院", "level": "专科"},
            {"code": "4133012790", "name": "台州职业技术学院", "level": "专科"},
            {"code": "4133012791", "name": "浙江工贸职业技术学院", "level": "专科"},
            {"code": "4133012860", "name": "浙江医药高等专科学校", "level": "专科"},
            {"code": "4133012861", "name": "浙江机电职业技术学院", "level": "专科"},
            {"code": "4133012862", "name": "浙江建设职业技术学院", "level": "专科"},
            {"code": "4133012863", "name": "浙江艺术职业学院", "level": "专科"},
            {"code": "4133012864", "name": "浙江经贸职业技术学院", "level": "专科"},
            {"code": "4133012865", "name": "浙江商业职业技术学院", "level": "专科"},
            {"code": "4133012866", "name": "浙江经济职业技术学院", "level": "专科"},
            {"code": "4133012867", "name": "浙江旅游职业学院", "level": "专科"},
            {"code": "4133012868", "name": "浙江育英职业技术学院", "level": "专科"},
            {"code": "4133012869", "name": "浙江警官职业学院", "level": "专科"},
            {"code": "4133012870", "name": "浙江金融职业学院", "level": "专科"},
            {"code": "4133012871", "name": "浙江工业职业技术学院", "level": "专科"},
            {"code": "4133012872", "name": "杭州职业技术学院", "level": "专科"},
            {"code": "4133012874", "name": "嘉兴职业技术学院", "level": "专科"},
            {"code": "4133012875", "name": "湖州职业技术学院", "level": "专科"},
            {"code": "4133012876", "name": "绍兴职业技术学院", "level": "专科"},
            {"code": "4133012877", "name": "衢州职业技术学院", "level": "专科"},
            {"code": "4133012878", "name": "丽水职业技术学院", "level": "专科"},
            {"code": "4133013002", "name": "浙江东方职业技术学院", "level": "专科"},
            {"code": "4133013003", "name": "义乌工商职业技术学院", "level": "专科"},
            {"code": "4133013025", "name": "浙江纺织服装职业技术学院", "level": "专科"},
            {"code": "4133013026", "name": "杭州科技职业技术学院", "level": "专科"},
            {"code": "4133013027", "name": "浙江长征职业技术学院", "level": "专科"},
            {"code": "4133013028", "name": "嘉兴南洋职业技术学院", "level": "专科"},
            {"code": "4133013029", "name": "浙江广厦建设职业技术学院", "level": "专科"},
            {"code": "4133013030", "name": "杭州万向职业技术学院", "level": "专科"},
            {"code": "4133013688", "name": "浙江邮电职业技术学院", "level": "专科"},
            {"code": "4133013742", "name": "宁波卫生职业技术学院", "level": "专科"},
            {"code": "4133013746", "name": "台州科技职业学院", "level": "专科"},
            {"code": "4133013853", "name": "浙江国际海运职业技术学院", "level": "专科"},
            {"code": "4133013854", "name": "浙江体育职业技术学院", "level": "专科"},
            {"code": "4133014088", "name": "温州科技职业学院", "level": "专科"},
            {"code": "4133014089", "name": "浙江汽车职业技术学院", "level": "专科"},
            {"code": "4133014090", "name": "浙江横店影视职业学院", "level": "专科"},
            {"code": "4133014269", "name": "浙江农业商贸职业学院", "level": "专科"},
            {"code": "4133014431", "name": "浙江特殊教育职业学院", "level": "专科"},
            {"code": "4133014492", "name": "浙江安防职业技术学院", "level": "专科"},
            {
                "code": "4133016408",
                "name": "浙江舟山群岛新区旅游与健康职业学院",
                "level": "专科"
            },
            {"code": "4233050559", "name": "宁波幼儿师范高等专科学校", "level": "专科"}
        ]
    
    def in_school_list(self):
        for item in self.SCHOOL_LIST:
            if item["name"] == self.text:
                return True
        return False

    # 如果采购名称里面有职业就全部换成职教，如果名称里面有小学/中学/学校都放成普教，如果in schoollist或者大学就都换成高教，剩下的填其他
    def get_customer_type(self):
        result = ''

        if self.is_school():
            if '职业' in self.text:
                result = '职教'
            # 这个分支必须在最后一个前面，因为大学有重叠，这个范围更小
            elif self.in_school_list():
                result = '高教'
            elif '小学' in self.text or '中学' in self.text or '大学' in self.text:
                result = '普教'
        else: 
            result = '其他'
        return result


    def is_school(self):
        school_keyword_list = ["小学", "中学", "大学","学院"]
        for school_keyword in school_keyword_list:
            if(school_keyword in self.text):
                return True
        return False


# test case

# list = [
#     "云和县云和中学",
#     "浙江师范大学", #X
#     "绍兴市稽山中学",
#     "龙泉市教育局",
#     "杭州职业技术学院",
#     "浙江工商大学",
#     "临安区教育保障中心"
# ]

# for item in list:
#     print(School(item).get_customer_type())



