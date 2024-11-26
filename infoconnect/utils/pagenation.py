import json
import math
from urllib.parse import parse_qs, urlparse
from infoconnect.utils.re.bj import Re_bj
from infoconnect.utils.re.hubei import Re_Hubei
import scrapy
from scrapy.selector import Selector
from infoconnect.conf.index import DEFAULT_QUERY_MAP, PLACE_MAP, SOURCE_MAP
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.nodeparse import NodeParse


def parse_page_info(spider, response, keyword):
    pageSize = 100
    totalPage = 0
    source_key = response.meta["source_key"]
    current_conf = SOURCE_MAP[source_key]
    query_base_url = current_conf["query_base_url"]

    current_query_conf = DEFAULT_QUERY_MAP[source_key]
    query_param = current_query_conf["query_default_param"]
    query_param[current_query_conf["search_key"]] = keyword

    spider.logger.debug(f'query_param in pageinfo: {query_param}')
    if "t" in query_param:
        # 删掉分页的标
        del query_param["t"]
    result_url_list = []
    json_param_list = []

    spider.logger.debug(
        f'source_key, query_param: {source_key}, {query_param}')

    # 浙江的结果直接是接口，json 来解析
    if source_key == PLACE_MAP["ZHEJIANG"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        spider.logger.debug('list responseStr')
        spider.logger.debug(responseStr)
        if responseJson["successFlag"] == True:
            pageSize = 100
            totalCount = responseJson["realCount"] or responseJson["count"]
            totalPage = math.ceil(totalCount / pageSize)
            spider.logger.debug(f'{totalCount}, {totalPage}')
            for current_page in range(totalPage):
                detail_query = query_param
                detail_query["pageNo"] = current_page + 1
                detail_url = UrlFactory(
                    query_base_url, detail_query).build()
                result_url_list.append(detail_url)
    # 北京
    elif source_key == PLACE_MAP["BEIJING"]:
        pageSize = 10
        selector = Selector(text=response.body).xpath('//body')
        text = NodeParse(selector).to_text()
        totalCount = Re_bj(text).total_count()

        # 存在查询不到的情况
        if totalCount is not '':
            totalPage = math.ceil(int(totalCount) / pageSize)
            for current_page in range(totalPage):
                detail_query = query_param
                detail_query["page"] = current_page + 1
                detail_url = UrlFactory(query_base_url, detail_query).build()
                result_url_list.append(detail_url)
    # 安徽
    elif source_key == PLACE_MAP["ANHUI"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        spider.logger.debug('list responseStr')
        spider.logger.debug(responseStr)

        if responseJson["timed_out"] == False:
            pageSize = 15
            if "hits" in responseJson and "total" in responseJson["hits"]:
                totalCount = responseJson["hits"]["total"]
                spider.logger.debug(f'totalCount: {totalCount}')
                totalPage = math.ceil(int(totalCount) / pageSize)
                for current_page in range(totalPage):
                    detail_query = query_param
                    detail_query["pageNo"] = current_page + 1
                    # detail_url = UrlFactory(
                    #     query_base_url, detail_query).build()
                    # post 格式变化的是参数
                    result_url_list.append(query_base_url)
                    json_param_list.append(detail_query)
    # 四川
    elif source_key == PLACE_MAP["SICHUAN"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        spider.logger.debug('list responseStr')
        spider.logger.debug(responseStr)

        if responseJson["code"] == "200":
            if 'total' in responseJson:
                totalCount = int(responseJson["total"])
                totalPage = math.ceil(int(totalCount) / pageSize)
                for current_page in range(totalPage):
                    detail_query = query_param
                    detail_query["currPage"] = current_page + 1
                    detail_url = UrlFactory(
                        query_base_url, detail_query).build()
                    result_url_list.append(detail_url)
    # 湖北
    elif source_key == PLACE_MAP["HUBEI"]:
        spider.logger.debug(f'HUBEI page')
        pageSize = 10
        selector = Selector(text=response.body).xpath('//body')
        text = NodeParse(selector).to_text()

        spider.logger.debug(f'HUBEI page')
        spider.logger.debug(response.body)
        spider.logger.debug(f'text')
        spider.logger.debug(text)
        spider.logger.debug(f'HUBEI page')
        totalCount = Re_Hubei(text).total_count()
        if totalCount is not '':
            spider.logger.debug(f'HUBEI totalCount: {totalCount} ')
            if totalCount:
                totalPage = math.ceil(int(totalCount) / pageSize)
                for current_page in range(totalPage):
                    detail_query = query_param
                    detail_query["queryInfo.pageNo"] = current_page + 1
                    result_url_list.append(query_base_url)
                    json_param_list.append(detail_query)
    # 河北
    elif source_key == PLACE_MAP["HEBEI"]:
        pageSize = 50
        spider.logger.debug('HEBEI page')
        # 如果数据小于 10条的时候没有分页条
        selector = Selector(text=response.body).xpath('//body')
        text = NodeParse(selector).to_text()

        list = Selector(text=response.body).xpath(
            '//a[@class="a3"]/@href').getall()
        last_page_link_list = Selector(text=response.body).xpath(
            '//a[@class="last-page"]/@href').getall()
        totalCount = 0
        totalPage = 0

        if len(list) <= 50:
            totalCount = len(list)
            totalPage = 1
        else:
            if len(last_page_link_list):
                last_page_link = last_page_link_list[0]
                page = parse_qs(urlparse(last_page_link).query)[
                    'page'][0]
                totalPage = page
        for current_page in range(totalPage):
            detail_query = query_param
            detail_query["page"] = current_page + 1
            detail_url = UrlFactory(
                query_base_url, detail_query).build()
            result_url_list.append(detail_url)
    # 上海
    elif source_key == PLACE_MAP["SHANGHAI"]:
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        spider.logger.debug('list responseStr')
        spider.logger.debug(responseStr)

        if responseJson["timed_out"] == False:
            pageSize = 15
            if "hits" in responseJson and "total" in responseJson["hits"]:
                totalCount = responseJson["hits"]["total"]
                spider.logger.debug(f'totalCount: {totalCount}')
                totalPage = math.ceil(int(totalCount) / pageSize)
                for current_page in range(totalPage):
                    detail_query = query_param
                    detail_query["pageNo"] = current_page + 1
                    # detail_url = UrlFactory(
                    #     query_base_url, detail_query).build()
                    # post 格式变化的是参数
                    result_url_list.append(query_base_url)
                    json_param_list.append(detail_query)

    spider.logger.debug(
        f'pageInfo pageSize, result_url_list, json_param_list : {pageSize}, {totalCount} ,{result_url_list} , {json_param_list}')

    return [result_url_list, json_param_list]
