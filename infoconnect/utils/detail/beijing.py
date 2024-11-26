import re
from urllib.parse import parse_qs, urlparse
from infoconnect.items import WinningNoticeItem
from infoconnect.utils.index import Utils
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.re.bj import Re_bj
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.school import School
from infoconnect.utils.urlfactory import UrlFactory
from scrapy.selector import Selector


def beijing_result_detail(spider, response):
    url = response.url
    html_doc = str(response.body, encoding="GBK")
    content_selector = Selector(
        text=html_doc).xpath('//div[@class="xl-main"]')
    text = NodeParse(content_selector).to_text()

    noticePubDate_text = Selector(text=html_doc).xpath(
        '//div[@class="xl-box-t"]//span/text()').get()

    util = Re_bj(text)

    spplier_name = util.spplier_name()

    projectCode = util.project_code()
    noticePubDate = noticePubDate_text
    winning_notice_url = url
    project_winning_amt = util.project_winning_amt()
    order_id = 1  # TODO
    winning_order_cnt = 1
    supplier_name = spplier_name
    supplier_addr = util.spplier_addr()
    order_name = util.project_name()
    winning_amt = util.winning_amt()
    cadidate_name = ''

    if len(spplier_name) > 1:
        winning_order_cnt = len(spplier_name)
        order_id_list = []
        for order_index in range(winning_order_cnt):
            order_id_list.append(str(order_index + 1))
        order_id = ','.join(order_id_list)

    # item = WinningNoticeItem()

    # buyer_contact = util.buyer_contact()
    # buyer_contact_person = ''
    # buyer_phone = ''

    # agency_contact = util.agency_contact()
    # agency_contact_person = ''
    # agency_phone = ''

    # if len(buyer_contact.split(",")) == 2:
    #     buyer_contact_person = buyer_contact.split(",")[0]
    #     buyer_phone = buyer_contact.split(",")[1]

    # if len(agency_contact.split(",")) == 2:
    #     agency_contact_person = agency_contact.split(",")[0]
    #     agency_phone = agency_contact.split(",")[1]
    # if len(agency_contact.split("，")) == 2:
    #     agency_contact_person = agency_contact.split("，")[0]
    #     agency_phone = agency_contact.split("，")[1]

    item = {}
    item["project_id"] = projectCode
    item["winning_date"] = noticePubDate
    item["winning_notice_url"] = winning_notice_url
    item["order_id"] = order_id
    item["winning_order_cnt"] = winning_order_cnt  # 中标标项cnt
    item["project_winning_amt"] = project_winning_amt  # 项目中标总金额

    # TODO 供应商中标信息有的是表格形式
    # http://www.ccgp-beijing.gov.cn/xxgg/qjzfcggg/qjzbjggg/t20220316_1412985.html
    item["supplier_name"] = supplier_name
    item["supplier_addr"] = supplier_addr
    item["order_name"] = order_name
    item["winning_amt"] = winning_amt
    item["cadidate_name"] = cadidate_name

    item["buyer_name"] = util.buyer_name()
    item["buyer_addr"] = util.buyer_addr()
    item["buyer_contact"] = util.buyer_contact()
    item["buyer_phone"] = ''

    item["agency_name"] = util.agent_name()
    item["agency_addr"] = util.agent_addr()
    item["agency_contact"] = util.agency_contact()
    item["agency_phone"] = ''
    item["source_id"] = response.meta["source_key"]

    return item
    # else:
    #     return None
