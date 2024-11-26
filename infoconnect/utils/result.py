import json
import math
import re
from urllib.parse import parse_qs, urlparse
from infoconnect.utils.re.bj import Re_bj
from scrapy.selector import Selector
from infoconnect.conf.index import PLACE_MAP, SOURCE_MAP
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.nodeparse import NodeParse, node_text


def parse_result_page(spider, response):
    source_key = response.meta["source_key"]
    source_map_conf = SOURCE_MAP[source_key]
    result_url_list = []

    spider.logger.debug('source_key')
    spider.logger.debug(source_key)

    # 浙江的结果直接是接口，json 来解析
    if source_key == PLACE_MAP["ZHEJIANG"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        # keyword = response.meta["keyword"]

        spider.logger.debug(
            f'responseJson in parse_result_page {responseJson}')

        if responseJson["successFlag"] == True:
            articles = responseJson["articles"]
            for article in articles:
                article_url = article['url']
                notice_id = parse_qs(urlparse(article_url).query)[
                    'noticeId'][0]
                detail_url = UrlFactory(source_map_conf['detail_base_url'], {
                                        "noticeId": notice_id}).build()

                spider.logger.debug(f'detail_url: {detail_url}')
                result_url_list.append(detail_url)
    elif source_key == PLACE_MAP["BEIJING"]:
        html_doc_string = response.body.decode('utf-8')
        # spider.logger.debug('html_doc_string')
        # spider.logger.debug(html_doc_string)

        # 这里对查询到的结果过滤，只保留中标公告
        result_link_list = Selector(text=html_doc_string).xpath(
            '//a[@class="searchresulttitle"]')

        for item in result_link_list:
            title_text = node_text(item)
            title_link = item.xpath("./@href").get()
            result_title = re.findall('中标公告$', title_text)
            if len(result_title):
                result_url_list.append(title_link)
    elif source_key == PLACE_MAP["ANHUI"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        if responseJson["timed_out"] == False:
            if "hits" in responseJson and "hits" in responseJson["hits"]:
                result_list = responseJson["hits"]["hits"]
                for item in result_list:
                    result_url_list.append(
                        f'{source_map_conf["home_page_url"]}{item["_source"]["url"]}')
    elif source_key == PLACE_MAP["SICHUAN"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        if responseJson["code"] == "200":
            if "data" in responseJson:
                result_list = responseJson["data"] or []
                for item in result_list:
                    result_url_list.append(
                        f'{source_map_conf["home_page_url"]}{item["pageurl"]}')
    elif source_key == PLACE_MAP["HUBEI"]:
        # TODO 接口还是有些问题
        spider.logger.debug(f'HUBEI page')
        selector = Selector(text=response.body).xpath('//body')
        text = NodeParse(selector).to_text()

        spider.logger.debug(f'HUBEI page')
        spider.logger.debug(response.body)
        spider.logger.debug(f'text')
        spider.logger.debug(text)
        spider.logger.debug(f'HUBEI page')

    elif source_key == PLACE_MAP["HEBEI"]:

        spider.logger.debug('HEBEI result')
        # spider.logger.debug(response.body.decode("utf-8"))

        # spider.logger.debug(response.url)
        # spider.logger.debug(response.body.decode("utf-8"))

        result_list = Selector(text=response.body).xpath(
            '//a[@class="a3"]/@href').getall()
        for item in result_list:
            result_url_list.append(item)
    elif source_key == PLACE_MAP["SHANGHAI"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        if responseJson["timed_out"] == False:
            if "hits" in responseJson and "hits" in responseJson["hits"]:
                result_list = responseJson["hits"]["hits"]
                for item in result_list:
                    result_url_list.append(
                        f'{source_map_conf["home_page_url"]}{item["_source"]["url"]}')

    return result_url_list
