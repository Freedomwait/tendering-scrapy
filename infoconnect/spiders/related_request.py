import json
import time
from infoconnect.utils.area.zhejiang import ZhejiangeArea
from infoconnect.utils.common_queryfactory import CommonQueryFactory
from infoconnect.utils.re.zhejiang import Re_Zhejiang
import scrapy
from scrapy.selector import Selector

import pandas as pd
from urllib.parse import urlparse, parse_qs
from infoconnect.utils.index import Utils, purchase_type
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.queryfactory import QueryFactory
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.school import School
from infoconnect.conf.index import DEFAULT_QUERY_MAP, PLACE_MAP, TASK, SOURCE_MAP, ALLOWED_DOMAINS


class RelatedRequestSpider(scrapy.Spider):
    name = 'related_request'
    allowed_domains = ALLOWED_DOMAINS

    start_urls = ['https://zfcg.czt.zj.gov.cn/purchaseNotice/index.html']

    detail_base_url = 'https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html'

    custom_settings = {
        "FEEDS": {
            f'out/related_request_{TASK["TASK_CODE"]}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/related_request_{TASK["TASK_CODE"]}.log',
        "LOG_FILE_APPEND": False
    }

    def __init__(self):
        super().__init__()
        # 读取common result的产物，获取项目编号列表
        # 按照项目编号组装请求获取对应的采购公告
        # 解析采购公告详情页

        pass

    def parse(self, response):
        relate_df = pd.read_csv(
            f'sql/related_project{TASK["TASK_CODE"]}.csv').dropna(axis=0, subset=[
                'request_id'], how='any')

        request_id_list = relate_df["request_id"].tolist()
        project_id_list = relate_df["project_code"].tolist()

        for item_index in range(len(request_id_list)):
            if request_id_list[item_index]:
                detail_url = UrlFactory(
                    'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results', {"noticeId": str(int(request_id_list[item_index])), "url": "noticeDetail"}).build()
                self.logger.info(detail_url)
                yield scrapy.Request(detail_url, meta={"project_id": project_id_list[item_index]}, callback=self.parse_detail)
        pass

    def parse_detail(self, response):
        url = response.url
        resJson = json.loads(response.body)
        item = {}
        selector = Selector(text=resJson['noticeContent']).xpath('//body')
        text = NodeParse(selector).to_text()
        util = Re_Zhejiang(text)

        notice_id = parse_qs(urlparse(url).query)[
            'noticeId'][0]
        page_url = UrlFactory(
            self.detail_base_url, {"noticeId": notice_id}).build()

        sourcing_type = purchase_type(resJson["noticeTitle"])
        district = resJson["district"]

        zhejiangeArea = ZhejiangeArea().get_areainfo_by_value(district)

        project_name = ''
        order_count = 1
        buyer_count = 1

        order_item_list = util.order_item_list()
        self.logger.debug('order_item_list')
        self.logger.debug(order_item_list)

        order_count = len(order_item_list)
        if sourcing_type == '公开招标':
            project_name = util.project_name()
        else:
            project_name = util.project_name_race()
            if sourcing_type == '竞争性磋商':
                order_count = 1

        noticePubDate = resJson["noticePubDate"]

        item["project_id"] = response.meta["project_id"]
        item["project_name"] = project_name
        item['sourcing_type'] = sourcing_type

        buyer_name = util.buyer_name()
        buyer_id = ''

        self.logger.debug('buyer_name')
        self.logger.debug(type(buyer_name))
        self.logger.debug(buyer_name)

        if len(buyer_name):
            buyer_name_list = buyer_name[0].split(",")
            buyer_count = len(buyer_name_list)
            buyer_id_list = []
            for buyer_index in range(buyer_count):
                buyer_id_list.append(str(buyer_index + 1))
            buyer_id = ','.join(buyer_id_list)

        item['province'] = zhejiangeArea['province']
        item['county'] = zhejiangeArea['county']
        item['district'] = zhejiangeArea['district']

        item['agency_name'] = util.bidding_agent_name()
        item['agency_addr'] = util.bidding_agent_purchaser_address()
        item['agency_contact'] = util.bidding_agent_purchaser_person()
        item['agency_phone'] = util.bidding_agent_purchaser_contact()

        item['request_date'] = noticePubDate
        item['closing_date'] = util.purchase_dead_line()

        item['order_count'] = order_count
        item['buyer_count'] = buyer_count

        item["project_max_amt"] = util.maximum_price()
        item["request_notice_url"] = page_url
        item["budget_amt"] = util.budget_price()
        item["buyer_id"] = buyer_id
        item["buyer_name"] = buyer_name
        item["buyer_addr"] = util.buyer_addr()
        item["buyer_contact"] = util.buyer_contact()
        item["buyer_phone"] = util.buyer_phone()
        item["source_id"] = '0'

        # item["text"] = text
        yield item

    def closed(self, reason):
        self.logger.info(f'spider detail closed {reason}')
        pass
