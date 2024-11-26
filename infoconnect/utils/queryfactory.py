from datetime import date, timedelta

# 页面搜索框
# https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results?pageSize=15&pageNo=1&type=20&keyword=%E9%BB%91%E6%9D%BF&isExact=1&url=fullTestCearch
# 采购公告搜索
# https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results?pageSize=15&pageNo=1&sourceAnnouncementType=3004%2C4005%2C4006&isGov=true&keyword=%E9%BB%91%E6%9D%BF&isExact=1&url=notice


class QueryFactory:
    def __init__(self):
        self.query = {
            "keyword": "",
            # "type": 20,
            # "url": "fullTestCearch",
            "sourceAnnouncementType": "3004,4005,4006",
            "url": "notice",
            "isExact": 1,
            "pageNo": 1,
            "pageSize": 100,
        }

    def keyword(self, keyword):
        self.query["keyword"] = keyword
        return self

    def type(self, type):
        self.query["type"] = type
        return self

    def isExact(self, isExact):
        # defalut is full content
        self.query["isExact"] = 0 if isExact == "title" else 1
        return self

    def pageNo(self, type):
        self.query["pageNo"] = type
        return self

    def pageSize(self, isExact):
        self.query["pageSize"] = isExact
        return self

    # 时间参数
    def time(self, type):
        if type == 'all':
            self.query["endDate"] = date.today()
            return self
        else:
            type_dict = {
                "today": date.today(),
                "last_three_day": self.format_day(3),
                "last_week": self.format_day(7),
                "last_month": self.format_day(30),
                "last_three_month": self.format_day(90),
                "last_half_year": self.format_day(180),
                "last_year": self.format_day(375),
            }

            self.query["pubDate"] = type_dict[type]
            self.query["endDate"] = date.today()
            return self

    def format_day(self, days):
        return (date.today() - timedelta(days=days)).strftime('%Y-%m-%d')

    def build(self):
        return self.query
