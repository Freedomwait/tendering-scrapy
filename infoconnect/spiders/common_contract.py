import json
import time
from infoconnect.utils.common_queryfactory import CommonQueryFactory
from infoconnect.utils.contract.shanghai import shanghai_contract_detail
from infoconnect.utils.contract.sichuan import sichuan_contract_detail
from infoconnect.utils.pagenation import parse_page_info
from infoconnect.utils.request.sichuan import sichuan_request_detail
from infoconnect.utils.result import parse_result_page
from infoconnect.utils.resultdetail import parse_result_detail
import scrapy
import pandas as pd
from urllib.parse import urlparse, parse_qs
from infoconnect.utils.index import Utils
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.queryfactory import QueryFactory
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.school import School
from infoconnect.conf.index import DEFAULT_QUERY_MAP, PLACE_MAP, TASK, SOURCE_MAP, ALLOWED_DOMAINS


class CommonContractSpider(scrapy.Spider):
    name = 'common_contract'
    allowed_domains = ALLOWED_DOMAINS

    start_urls = [
        'http://www.ccgp-beijing.gov.cn/xxgg/index.html?name=jieshou']

    custom_settings = {
        "FEEDS": {
            f'out/common_contract_{TASK["TASK_CODE"]}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/common_contract_{TASK["TASK_CODE"]}.log',
        "LOG_FILE_APPEND": False
    }

    def __init__(self):
        super().__init__()

        # 读取common result的产物，获取项目编号列表
        # 按照项目编号组装请求获取对应的采购公告
        # 解析采购公告详情页
        pass

    def parse(self, response):
        common_result_df = pd.read_csv(
            f'out/common_result_{TASK["TASK_CODE"]}.csv').dropna(axis=0, subset=[
                'project_id'], how='any')

        # common_result_df = pd.read_csv(
        #     f'out/test.csv').dropna(axis=0, subset=[
        #         'project_id'], how='any')

        for index, row in common_result_df.iterrows():
            project_id = row["project_id"]
            source_id = str(row["source_id"])
            reuqest_url = ''
            if source_id == PLACE_MAP["SICHUAN"]:
                # reuqest_url = project_id
                # http: // www.ccgp-sichuan.gov.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do?currPage = 1 & pageSize = 10 & noticeType = 00101 & regionCode = &purchaseManner = &title = &openTenderCode = N5105032022000072 & purchaser = &agency = &purchaseNature = &operationStartTime = &operationEndTime = &selectTimeName = noticeTime & cityOrArea =
                reuqest_url = UrlFactory(
                    'http://www.ccgp-sichuan.gov.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do',
                    {
                        "noticeType": "001054",
                        "selectTimeName": "noticeTime",
                        "pageSize": 10,
                        "currPage": 1,
                        "openTenderCode": project_id
                    }
                ).build()
                yield scrapy.Request(reuqest_url, meta={"source_id": source_id, "project_id": project_id}, callback=self.parse_item)
                # elif source_id == PLACE_MAP["BEIJING"]:
                #     reuqest_url = project_id
            elif source_id == PLACE_MAP["SHANGHAI"]:
                yield scrapy.http.JsonRequest(url='http://www.zfcg.sh.gov.cn/front/search/category',
                                              meta={"source_id": source_id,
                                                    "project_id": project_id},
                                              data={
                                                  "categoryCode": "ZcyAnnouncement5",
                                                  "pageNo": "1",
                                                  "pageSize": "15",
                                                  "projectCode": project_id
                                              },
                                              callback=self.parse_item)

    def parse_item(self, response):
        source_id = str(response.meta['source_id'])
        project_id = str(response.meta['project_id'])

        request_item = {}

        if source_id == PLACE_MAP["SICHUAN"]:
            request_item = sichuan_contract_detail(self, response)
            yield request_item
        elif source_id == PLACE_MAP["SHANGHAI"]:
            responseStr = str(response.body, encoding="utf-8")
            responseJson = json.loads(responseStr)
            if responseJson["timed_out"] == False:
                if "hits" in responseJson and "hits" in responseJson["hits"]:
                    result_list = responseJson["hits"]["hits"]
                    for item in result_list:
                        source_data = item["_source"]
                        notice_url = f'http://www.zfcg.sh.gov.cn{source_data["url"]}'
                        procurementMethod = source_data['procurementMethod']
                        yield scrapy.Request(notice_url, meta={
                            "source_id": source_id,
                            "project_id": project_id,
                            "procurementMethod": procurementMethod,
                        },
                            callback=self.parse_item_detail)
            # request_item = shanghai_contract_detail(self, response)

    def parse_item_detail(self, response):
        request_item = {}
        request_item = shanghai_contract_detail(self, response)

        yield request_item

    def closed(self, reason):
        self.logger.info(f'spider detail closed {reason}')
        pass
