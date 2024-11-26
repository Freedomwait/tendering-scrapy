import datetime
import json
import re
from urllib.parse import parse_qs, urlparse
from infoconnect.items import WinningNoticeItem
from infoconnect.utils.index import Utils
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.re.anhui import Re_anhui
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.school import School
from infoconnect.utils.urlfactory import UrlFactory
from scrapy.selector import Selector


def anhui_result_detail(spider, response):
    url = response.url
    selector = Selector(text=response.body.decode('utf-8')).xpath('//body')
    text = NodeParse(selector).to_text()

    util = Re_anhui(text)

    projectCode = util.project_code()
    noticePubDate = ''
    winning_notice_url = url
    order_id = ''
    winning_order_cnt = ''
    supplier_name = util.spplier_name()
    supplier_addr = ''
    order_name = util.project_name()
    winning_amt = ''
    cadidate_name = ''

    # item = WinningNoticeItem()
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
    item["cadidate_name"] = cadidate_name,
    # item["text"] = text
    item["text"] = text

    return item
