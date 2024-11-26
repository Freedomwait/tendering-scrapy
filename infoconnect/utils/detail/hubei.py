import datetime
import json
import re
from urllib.parse import parse_qs, urlparse
from infoconnect.items import WinningNoticeItem
from infoconnect.utils.index import Utils
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.school import School
from infoconnect.utils.urlfactory import UrlFactory
from scrapy.selector import Selector


def hubei_result_detail(spider, response):
    url = response.url
    selector = Selector(text=response.body.decode('utf-8')).xpath('//body')
    text = NodeParse(selector).to_text()

    projectCode = ''
    noticePubDate = ''
    winning_notice_url = ''
    order_id = ''
    winning_order_cnt = ''
    supplier_name = ''
    supplier_addr = ''
    order_name = ''
    projectCode = ''
    winning_amt = ''
    cadidate_name = ''

    item = WinningNoticeItem()
    item["project_id"] = projectCode
    item["winning_date"] = noticePubDate
    item["winning_notice_url"] = url
    item["order_id"] = order_id
    item["winning_order_cnt"] = winning_order_cnt  # 中标标项cnt
    item["project_winning_amt"] = ''  # 项目中标总金额
    item["supplier_name"] = supplier_name
    item["supplier_addr"] = supplier_addr
    item["order_name"] = order_name
    item["winning_amt"] = winning_amt
    item["cadidate_name"] = cadidate_name,
    # item["text"] = text
    item["text"] = text

    return item
