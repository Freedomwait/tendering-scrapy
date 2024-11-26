import datetime
import json
import re
from urllib.parse import parse_qs, urlparse
from infoconnect.items import WinningNoticeItem
from infoconnect.utils.index import Utils, parse_table, parse_table_with_header
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.re.hebei import Re_hebei
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.school import School
from infoconnect.utils.urlfactory import UrlFactory
from scrapy.selector import Selector


def hebei_result_detail(spider, response):
    url = response.url
    html_doc = response.body.decode('utf-8')
    #  优先解析新版本
    selector = Selector(text=html_doc).xpath('//table[@id="2020_VERSION"]')
    text = NodeParse(selector).to_text()
    util = Re_hebei(text)

    projectCode = util.project_id()
    noticePubDate = util.publish_date()
    winning_notice_url = parse_qs(urlparse(url).query)[
        'url'][0]
    order_id = 1
    winning_order_cnt = 1
    order_name = util.order_name()
    cadidate_name = ''

    supplier_name = ''
    supplier_addr = ''
    winning_amt = ''

    # 供应商表格
    supplier_table = Selector(text=html_doc).xpath(
        '//table[@id="SupplierInfos"]')
    if len(supplier_table):
        rows_header = supplier_table.xpath(".//tr//th/text()").getall()
        rows_body = supplier_table.xpath(".//tr//td/text()").getall()
        supplier_name = parse_table_with_header(
            rows_header, rows_body, "供应商名称")
        supplier_addr = parse_table_with_header(
            rows_header, rows_body, "供应商地址")

    main_subject_table_ids = [
        "EngineeringSupplierInfo",
        "GoodsSupplierInfo"
    ]
    for table_id in main_subject_table_ids:
        main_subject_table = Selector(text=html_doc).xpath(
            f'//table[@id="{table_id}"]')
        if len(main_subject_table):
            rows_header = main_subject_table.xpath(".//tr//th/text()").getall()
            rows_body = main_subject_table.xpath(".//tr//td/text()").getall()
            winning_amt = parse_table_with_header(
                rows_header, rows_body, "中标金额")
            break

    buyer_contact = util.buyer_contact()
    buyer_contact_person = ''.join(re.findall(
        "[\u4e00-\u9fa5]", buyer_contact)) or ''
    buyer_phone = ''.join(re.findall(
        "[^\u4e00-\u9fa5]", buyer_contact)) or ''

    agent_contact = util.agent_contact()
    agency_contact_person = ''.join(re.findall(
        "[\u4e00-\u9fa5]", agent_contact)) or ''
    agency_phone = ''.join(re.findall(
        "[^\u4e00-\u9fa5]", agent_contact)) or ''

    item = {}
    item["project_id"] = projectCode
    item["winning_date"] = noticePubDate
    item["winning_notice_url"] = winning_notice_url
    item["order_id"] = order_id
    item["winning_order_cnt"] = winning_order_cnt  # 中标标项cnt
    item["project_winning_amt"] = ''  # 项目中标总金额
    item["supplier_name"] = supplier_name
    item["supplier_addr"] = supplier_addr
    item["order_name"] = order_name
    item["winning_amt"] = winning_amt
    item["cadidate_name"] = cadidate_name
    item["buyer_name"] = util.buyer_name()
    item["buyer_addr"] = util.buyer_addr()
    item["buyer_contact"] = buyer_contact_person
    item["buyer_phone"] = buyer_phone

    item["agency_name"] = util.agent_name()
    item["agency_addr"] = util.agent_addr()
    item["agency_contact"] = agency_contact_person
    item["agency_phone"] = agency_phone

    return item
