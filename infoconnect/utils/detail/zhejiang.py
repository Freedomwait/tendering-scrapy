import datetime
import json
import re
from urllib.parse import parse_qs, urlparse
from infoconnect.items import WinningNoticeItem
from infoconnect.utils.index import Utils, parse_table, parse_table_with_header
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.school import School
from infoconnect.utils.urlfactory import UrlFactory
from scrapy.selector import Selector
import pandas as pd


def zhejiang_result_detail(spider, response):
    url = response.url
    resJson = json.loads(response.body)
    projectCode = resJson["projectCode"]
    noticePubDate = resJson["noticePubDate"]

    notice_id = parse_qs(urlparse(url).query)[
        'noticeId'][0]
    winning_notice_url = UrlFactory('https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html', {
        "noticeId": notice_id
    }).build()

    selector = Selector(text=resJson["noticeContent"]).xpath('//body')
    text = NodeParse(selector).to_text()
    util = Re_Zhejiang(text)

    # winning_amt = ''
    # supplier_name = ''
    # supplier_addr = ''
    cadidate_name = ''
    # order_id = ''
    order_name = ''
    winning_order_cnt = ''
    table_list = Selector(
        text=resJson['noticeContent']).xpath('//table')

    for table in table_list:
        rows_header = table.xpath('.//tr//th//text()').getall() or []
        rows_body = table.xpath('.//tr//td//text()').getall() or []

        spider.logger.debug('zhejiang_result_detail rows_header rows_body : ')
        spider.logger.debug('rows_header')
        spider.logger.debug(rows_header)
        spider.logger.debug('rows_body')
        spider.logger.debug(rows_body)

        table_text = node_text(table)

        spider.logger.debug('zhejiang_result_detail table_text: ')
        spider.logger.debug(table_text)

        if (table_text.find('标的名称') != -1):
            spider.logger.info('标的表格')

            table_headers = table.xpath(
                ".//tr[@class='firstRow']//td").getall()

            spider.logger.info(table_headers)
            # 列数
            col_number = len(table_headers)

            spider.logger.info(table_headers)
            spider.logger.info(col_number)

            if col_number:
                target_name = parse_table(
                    rows_body, col_number, "标项名称")

                spider.logger.debug("标项名称")
                spider.logger.debug(type(target_name))
                spider.logger.debug(target_name)
                if isinstance(target_name, list):
                    order_name = ','.join(target_name)
                elif isinstance(target_name, str):
                    order_name = target_name

        if (table_text.find('技术得分') != -1 or table_text.find('专家') != -1):
            spider.logger.info('专家技术评分明细表')
            cadidate_name_list = []

            for table_row in rows_body:
                if '公司' in table_row:
                    cadidate_name_list.append(table_row)

            cadidate_name = ','.join(cadidate_name_list)

            pass

    order_id_list = Selector(text=resJson["noticeContent"]).xpath(
        '//td[@class="code-sectionNo"]/text()').getall()
    supplier_name_list = Selector(text=resJson["noticeContent"]).xpath(
        '//td[@class="code-winningSupplierName"]/text()').getall()
    supplier_addr_list = Selector(text=resJson["noticeContent"]).xpath(
        '//td[@class="code-winningSupplierAddr"]/text()').getall()
    order_amt_list = Selector(text=resJson["noticeContent"]).xpath(
        '//td[@class="code-summaryPrice"]/text()').getall()

    # 相关文章
    relevantArticles = resJson['relevantArticles'] or []
    if (len(relevantArticles)):
        request_list = []
        result_list = []
        # 合同公告是一个列表
        contract_list = []

        for item in relevantArticles:
            # 招标类型2，中标类型5，合同公告 6
            if item["type"] == 2 and item["id"]:
                request_list.append(str(item["id"]))
            if item["type"] == 5 and item["id"]:
                result_list.append(str(item["id"]))
                # 合同公告
            if item["type"] == 6 and item["id"]:
                contract_list.append(str(item["id"]))

        # 插入一行新的
        spider.related_data_frame.loc[len(spider.related_data_frame)] = [
            projectCode, ','.join(request_list), ','.join(result_list), ','.join(contract_list)]

    winning_order_cnt = str(len(order_id_list))

    # item = WinningNoticeItem()
    item = {}
    item["project_id"] = projectCode,
    item["winning_date"] = noticePubDate,
    item["winning_notice_url"] = winning_notice_url
    item["order_id"] = ','.join(order_id_list),
    item["winning_order_cnt"] = winning_order_cnt,
    item["project_winning_amt"] = '',  # 项目中标总金额
    item["supplier_name"] = ",".join(supplier_name_list),
    item["supplier_addr"] = ",".join(supplier_addr_list),
    item["order_name"] = order_name,
    item["winning_amt"] = ",".join(order_amt_list),
    item["cadidate_name"] = cadidate_name,
    # item["text"] = text
    # item["text"] = ''

    return item
