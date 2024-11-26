
import scrapy
from scrapy.selector import Selector
import json
from infoconnect.conf.index import TASK
from infoconnect.utils.index import Utils, purchase_type
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.nodeparse import NodeParse


class NoticeSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['zfcgmanager.czt.zj.gov.cn']

    detail_url_base = 'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results'

    detail_base_url = "https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html"

    custom_settings = {
        "FEEDS": {
            f'out/price_{TASK["TASK_CODE"]}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/price_{TASK["TASK_CODE"]}.log',
        "LOG_FILE_APPEND": False
    }

    start_urls = [
        'https://zfcg.czt.zj.gov.cn/'
    ]

    need_list = []

    def __init__(self):
        super().__init__()
        file = open(
            f'sql/related_purchase_announcement{TASK["TASK_CODE"]}.txt', "r")
        fileLines = file.readlines()
        for line in fileLines:
            self.need_list.append(line)

        file.close()
        pass

    def parse(self, response):
        if len(self.need_list):
            for item in self.need_list:
                list = item.split(",")
                notice_id = list[0]
                purchase_id = list[1]

                detail_url = UrlFactory(
                    self.detail_url_base, {"noticeId": purchase_id, "url": "noticeDetail"}).build()
                yield scrapy.Request(detail_url, meta={"notice_id": notice_id, 'purchase_id': purchase_id}, callback=self.parse_item)

    def parse_item(self, response):
        url = response.url
        resJson = json.loads(response.body)
        item = {}
        selector = Selector(text=resJson['noticeContent']).xpath('//body')
        text = NodeParse(selector).to_text()
        util = Utils(text, url)

        page_url = UrlFactory(
            self.detail_base_url, {"noticeId": response.meta["notice_id"]}).build()
        item["网站链接"] = page_url
        item["最高限价"] = util.maximum_price()
        item["采购截止时间"] = util.purchase_dead_line()
        item['招采类型'] = purchase_type(resJson["noticeTitle"])
        item["采购noticeId"] = response.meta["purchase_id"]
        item["标项序号"] = util.project_count()
        item["标项名称"] = util.project_name()

        if purchase_type(resJson["noticeTitle"]) == '竞争性磋商':
            item["标项名称"] = util.project_name_race()
        item["text"] = text
        yield item

    def closed(self, reason):
        print(f'spider detail closed {reason}')
        pass
