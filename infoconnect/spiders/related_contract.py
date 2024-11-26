import json
import time
from infoconnect.utils.common_queryfactory import CommonQueryFactory
from infoconnect.utils.pagenation import parse_page_info
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.result import parse_result_page
from infoconnect.utils.resultdetail import parse_result_detail
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


class RelatedContractSpider(scrapy.Spider):
    name = 'related_contract'
    allowed_domains = ALLOWED_DOMAINS

    start_urls = ['https://zfcg.czt.zj.gov.cn/purchaseNotice/index.html']

    detail_base_url = "https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html"

    custom_settings = {
        "FEEDS": {
            f'out/related_contract_{TASK["TASK_CODE"]}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/related_contract_{TASK["TASK_CODE"]}.log',
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
                'contract_id'], how='any')

        contract_id_list = relate_df["contract_id"].tolist()
        project_id_list = relate_df["project_code"].tolist()

        for item_index in range(len(contract_id_list)):
            item = contract_id_list[item_index]
            project_id = project_id_list[item_index]
            if item:
                item_list = item.split(',') or []
                contract_cnt = len(item_list)
                for item_id_index in range(len(item_list)):
                    item_id = item_list[item_id_index]
                    order_id = str(item_id_index + 1)
                    detail_url = UrlFactory(
                        'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results', {"noticeId": str(int(item_id)), "url": "noticeDetail"}).build()
                    self.logger.info(detail_url)
                    yield scrapy.Request(detail_url, meta={"project_id": project_id, "contract_cnt": contract_cnt, "order_id": order_id}, callback=self.parse_detail)
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

        item["project_id"] = response.meta["project_id"]
        item["order_id"] = response.meta["order_id"]
        item["contract_id"] = util.contract_id()
        item['buyer_id'] = response.meta["order_id"]
        item["contract_amt"] = util.contract_amt()
        item["contract_notice_url"] = page_url
        item["contract_cnt"] = response.meta["contract_cnt"]

        # item["text"] = text
        yield item

    def closed(self, reason):
        self.logger.info(f'spider detail closed {reason}')
        pass
