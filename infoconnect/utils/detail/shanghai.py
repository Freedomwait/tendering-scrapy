import datetime
import json
import re
from urllib.parse import parse_qs, urlparse
from infoconnect.items import WinningNoticeItem
from infoconnect.utils.index import Utils, parse_table
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.re.shanghai import Re_Shanghai
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.school import School
from infoconnect.utils.urlfactory import UrlFactory
from scrapy.selector import Selector


def shanghai_result_detail(spider, response):
    url = response.url
    order_id = ''
    winning_order_cnt = 1
    supplier_name = ''
    supplier_addr = ''
    order_name = ''
    winning_amt = ''
    target_name = ''
    cadidate_name = ''

    html_doc = response.body.decode('utf-8')
    # selector = Selector(text=html_doc).xpath('//body')
    detailJsonData = Selector(text=html_doc).xpath(
        '//input[@name="articleDetail"]/@value').get()

    detail_json = json.loads(detailJsonData)

    spider.logger.info('shanghai_result_detail')
    spider.logger.info(detail_json)

    content_doc = Selector(text=detail_json["content"]).xpath(
        '//body')
    text = NodeParse(content_doc).to_text()

    table_list = Selector(text=detail_json["content"]).xpath(
        '//table')

    for table in table_list:
        rows_header = table.xpath('.//tr//th//text()').getall() or []
        rows_body = table.xpath('.//tr//td//text()').getall() or []

        table_text = node_text(table)

        spider.logger.debug('zhejiang_result_detail rows_header rows_body : ')
        spider.logger.debug('rows_header')
        spider.logger.debug(rows_header)
        spider.logger.debug('rows_body')
        spider.logger.debug(rows_body)

        if (table_text.find('中标供应商名称') != -1):

            table_headers = table.xpath(
                ".//tr//td").getall()

            table_row_length = len(table.xpath(".//tr"))
            table_td_length = len(table.xpath(".//td"))

            col_number = int(table_td_length / table_row_length)

            spider.logger.info(table_headers)
            spider.logger.info(col_number)

            if col_number:
                order_id = parse_table(
                    rows_body, col_number, "序号")
                target_name = parse_table(
                    rows_body, col_number, "标项名称")
                winning_amt = parse_table(
                    rows_body, col_number, "中标（成交金额）")
                supplier_name = parse_table(
                    rows_body, col_number, "中标供应商名称")
                supplier_addr = parse_table(
                    rows_body, col_number, "中标供应商地址")

                winning_order_cnt = len(order_id)
                if isinstance(target_name, list):
                    order_name = ','.join(target_name)
                elif isinstance(target_name, str):
                    order_name = target_name

            pass

        if (table_text.find('标的名称') != -1):

            pass

    util = Re_Shanghai(text)

    # item = WinningNoticeItem()
    item = {}
    item["project_id"] = detail_json["projectCode"]
    item["winning_date"] = detail_json["publishDate"]
    item["winning_notice_url"] = url
    item["order_id"] = order_id
    item["winning_order_cnt"] = winning_order_cnt  # 中标标项cnt
    item["project_winning_amt"] = ''  # 项目中标总金额
    item["supplier_name"] = supplier_name
    item["supplier_addr"] = supplier_addr
    item["order_name"] = order_name
    item["winning_amt"] = winning_amt
    item["cadidate_name"] = cadidate_name,

    item["buyer_name"] = util.buyer_name()
    item["buyer_addr"] = util.buyer_addr()
    item["buyer_contact"] = util.buyer_contact()
    item["buyer_phone"] = util.buyer_phone()

    item['agency_name'] = util.bidding_agent_name()
    item['agency_addr'] = util.bidding_agent_purchaser_address()
    item['agency_contact'] = util.bidding_agent_purchaser_person()
    item['agency_phone'] = util.bidding_agent_purchaser_contact()
    item["source_id"] = response.meta["source_key"]

    return item
