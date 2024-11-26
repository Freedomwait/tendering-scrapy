import time
import pandas as pd
from infoconnect.utils.pagenation import parse_page_info
from infoconnect.utils.result import parse_result_page
from infoconnect.utils.resultdetail import parse_result_detail
import scrapy
from scrapy.selector import Selector
from urllib.parse import urlparse, parse_qs
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.conf.index import DEFAULT_QUERY_MAP, PLACE_MAP, TASK, SOURCE_MAP, ALLOWED_DOMAINS


class CommonResultSpider(scrapy.Spider):
    name = 'common_result'
    allowed_domains = ALLOWED_DOMAINS

    start_urls = ['http://www.ccgp-beijing.gov.cn']

    custom_settings = {
        "FEEDS": {
            f'out/common_result_{TASK["TASK_CODE"]}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/common_result_{TASK["TASK_CODE"]}.log',
        "LOG_FILE_APPEND": False
    }

    def __init__(self):
        super().__init__()
        self.logger.info("=====  start task  ======")
        self.logger.info(TASK)

        d = {'project_code': [], 'request_id': [],
             'result_id': [], 'contract_id': []}
        self.related_data_frame = pd.DataFrame(data=d)
        pass

    def parse(self, response):

        # test item
        # yield scrapy.Request("https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results?noticeId=9022718&url=noticeDetail", meta={"source_key": "浙江", "keyword": "智慧教室"}, callback=self.parse_detail)

        for source_key, source_config in SOURCE_MAP.items():
            self.logger.debug(source_key)
            self.logger.debug(source_config)
            home_page_url = source_config["home_page_url"]
            query_base_url = source_config["query_base_url"]
            query_method = source_config["query_method"]
            keyword_list = source_config["keyword_list"]

            # self.logger.debug(f'query_method: {query_method}')

            for keyword in keyword_list:
                current_query_conf = DEFAULT_QUERY_MAP[source_key]
                query_param = current_query_conf["query_default_param"]
                query_param[current_query_conf["search_key"]] = keyword
                # 防止后面被当作重复请求
                query_param["t"] = str(int(round(time.time()) * 1000))
                meta_obj = {"source_key": source_key, "keyword": keyword}

                if query_method == 'GET':
                    search_url = UrlFactory(
                        query_base_url, query_param).build()
                    yield scrapy.Request(search_url,
                                         meta=meta_obj,
                                         callback=self.parse_list)
                elif query_method == 'JSON_POST':
                    yield scrapy.http.JsonRequest(url=query_base_url,
                                                  meta=meta_obj,
                                                  data=query_param,
                                                  callback=self.parse_list)
                elif query_method == 'FORM_POST':
                    yield scrapy.FormRequest(url=query_base_url,
                                             headers={
                                                 'Referer': home_page_url},
                                             meta=meta_obj,
                                             formdata=query_param,
                                             callback=self.parse_list)
                # self.logger.debug(f'search_url: {search_url}')

    def parse_list(self, response):
        # 处理分页，构造出分页列表
        source_key = response.meta["source_key"]
        current_conf = SOURCE_MAP[source_key]
        query_method = current_conf["query_method"]
        home_page_url = current_conf["home_page_url"]
        keyword = response.meta["keyword"]

        [pagenation_url_list, json_param_list] = parse_page_info(
            self, response, keyword=keyword)

        self.logger.debug(
            f'after parse_page_info: {pagenation_url_list}, {json_param_list}')
        if query_method == 'GET':
            for page_url in pagenation_url_list:
                self.logger.debug(f'page_url: {page_url}')
                yield scrapy.Request(page_url, meta={"source_key": source_key, "keyword": keyword}, callback=self.parse_list_result, dont_filter=True)
        elif query_method == 'JSON_POST':
            for url_index in range(len(pagenation_url_list)):
                yield scrapy.http.JsonRequest(url=pagenation_url_list[url_index],
                                              meta={"source_key": source_key,
                                                    "keyword": keyword},
                                              data=json_param_list[url_index],
                                              callback=self.parse_list_result,
                                              dont_filter=True)
        elif query_method == 'FORM_POST':
            for url_index in range(len(pagenation_url_list)):
                yield scrapy.FormRequest(url=pagenation_url_list[url_index],
                                         headers={
                    'Referer': home_page_url},
                    meta={"source_key": source_key, "keyword": keyword},
                    formdata=json_param_list[url_index],
                    callback=self.parse_list_result, dont_filter=True)

    def parse_list_result(self, response):
        self.logger.debug(f'parse_list_result from url: {response.url}')
        source_key = response.meta["source_key"]
        result_url_list = parse_result_page(self, response)
        self.logger.debug('result_url_list')
        self.logger.debug(result_url_list)

        for result_url in result_url_list:
            detail_url = result_url
            if source_key == PLACE_MAP["ZHEJIANG"]:
                # current_conf = SOURCE_MAP["ZHEJIANG"]
                notice_id = parse_qs(urlparse(result_url).query)[
                    'noticeId'][0]
                detail_url = UrlFactory('https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results', {
                    "noticeId": notice_id,
                    "url": "noticeDetail"
                }).build()
            elif source_key == PLACE_MAP["HEBEI"]:
                detail_url = UrlFactory("http://localhost:8050/render.html", {
                    "url": result_url
                }).build()
            yield scrapy.Request(detail_url, meta={"source_key": response.meta["source_key"], "keyword": response.meta["keyword"]}, callback=self.parse_detail)

    def parse_detail(self, response):
        self.logger.debug(f'parse_detail from url: {response.url}')
        item = parse_result_detail(self, response)
        # 过滤的排除
        if item is not None:
            item["source_id"] = response.meta["source_key"]
            item["keyword"] = response.meta["keyword"]
            yield item

    def closed(self, reason):
        self.logger.info(f'spider detail closed {reason}')
        self.related_data_frame.to_csv(
            f'sql/related_project{TASK["TASK_CODE"]}.csv')
        pass
