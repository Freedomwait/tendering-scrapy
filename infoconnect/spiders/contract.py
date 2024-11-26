
import scrapy
from scrapy.selector import Selector
import json
from infoconnect.conf.index import TASK
from infoconnect.utils.index import Utils
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.nodeparse import NodeParse


class NoticeSpider(scrapy.Spider):
    name = 'contract'
    allowed_domains = ['zfcgmanager.czt.zj.gov.cn']

    detail_url_base = 'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results'

    detail_base_url = "https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html"

    custom_settings = {
        "FEEDS": {
            f'out/contract_{TASK["TASK_CODE"]}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/contract_{TASK["TASK_CODE"]}.log',
        "LOG_FILE_APPEND": False
    }

    start_urls = [
        'https://zfcg.czt.zj.gov.cn/'
    ]

    need_list = []

    def __init__(self):
        super().__init__()
        file = open(
            f'sql/related_contract_announcement{TASK["TASK_CODE"]}.txt', "r")
        fileLines = file.readlines()
        for line in fileLines:
            self.need_list.append(line)

        file.close()
        pass

    def parse(self, response):
        if len(self.need_list):
            for item in self.need_list:
                # 因为合同存在多个，这里用 [] 来定位
                left_index = item.find("[")
                right_index = item.find("]")

                notice_id = item[:left_index - 1]

                # 多个合同公告
                contract_ids = item[left_index + 1:right_index]

                # print(f'item: {item}')
                # print(f'notice_id: {notice_id}')
                # print(f'contract_ids: {contract_ids}')

                # 过滤空值
                if (len(contract_ids)):
                    # 从文本中读出来的是 str 而不是 list
                    contract_ids_list = contract_ids.replace(
                        "'", '').replace(" '", '').split(",")
                    for contract_id in contract_ids_list:
                        detail_url = UrlFactory(
                            self.detail_url_base, {"noticeId": contract_id, "url": "noticeDetail"}).build()

                        # print(detail_url)
                        yield scrapy.Request(detail_url, meta={"notice_id": notice_id, 'contract_id': contract_id}, callback=self.parse_item)

    def parse_item(self, response):
        url = response.url
        resJson = json.loads(response.body)
        item = {}

        page_url = UrlFactory(
            self.detail_base_url, {"noticeId": response.meta["notice_id"]}).build()
        item["网站链接"] = page_url
        item['合同noticeId'] = str(response.meta['contract_id'])

        selector = Selector(text=resJson['noticeContent']).xpath('//body')
        text = NodeParse(selector).to_text()
        util = Utils(text, url)

        # jsonData 上有值的才能进行直接提取，如果没有的话，降级使用页面 富文本提取
        if resJson['jsonData']:
            res = json.loads(resJson['jsonData'])
            item["合同编号"] = res['contractCode']
            item["供应商联系方式"] = res['supplierContact']
            # 主要标的信息
            # mainSubjectInfo = res["mainSubjectInfo"]
            # [
            #         {
            #         unit: "4806.00",
            #         mainSubjectName: "智能灯光改造教室",
            #         specAndModel: "品牌:中教照明\n规格型号:详见投标文件",
            #         count: "631.00",
            #         sectionNo: "1",
            #         },
            #         {
            #         unit: "454.00",
            #         mainSubjectName: "普通灯光改造教室",
            #         specAndModel: "品牌:中教照明\n规格型号:详见投标文件",
            #         count: "196.00",
            #         sectionNo: "2",
            #         },
            #     ]
            # item["mainSubjectInfo"] = mainSubjectInfo
            # if len(mainSubjectInfo):
            #     for subject in mainSubjectInfo:
            #         mainSubjectName = subject["mainSubjectName"]
            #         sectionNo = subject["sectionNo"]
            #         item["标项序号"] = sectionNo
            #         item["标项名称"] = mainSubjectName
            #         yield item
            # else:
            #     yield item

        else:
            item["合同编号"] = util.contractCode()
            item["供应商联系方式"] = util.supplierContact()
            # mainSubjectInfo = util.mainSubjectInfo()
            # item["mainSubjectInfo"] = mainSubjectInfo
            # item["text"] = text
            # if len(mainSubjectInfo):
            #     for subject in mainSubjectInfo:
            #         mainSubjectName = subject["mainSubjectName"]
            #         sectionNo = subject["sectionNo"]
            #         item["标项序号"] = sectionNo
            #         item["标项名称"] = mainSubjectName
            #         yield item
            # else:
            #     item["text"] = text
            #     yield item
        item["text"] = text
        yield item

    def closed(self, reason):
        print(f'spider contract closed {reason}')
        pass
