from infoconnect.utils.nodeparse import NodeParse
from infoconnect.utils.re.sichuan import Re_Sichuan
from scrapy.selector import Selector


def sichuan_result_detail(spider, response):
    url = response.url

    winning_notice_url = url
    order_id = 1
    winning_order_cnt = 1
    order_name = ''
    winning_amt = ''
    cadidate_name = ''

    html_doc = response.body.decode('utf-8')
    selector = Selector(text=html_doc).xpath('//div[@id="print-content"]')
    text = NodeParse(selector).to_text()

    # 中标结果表格,可能有多个
    notice_result_table = Selector(text=html_doc).xpath(
        '//div[@id="_notice_content_noticeBidResult-noticeBidResult"]//table')

    supplier_name_list = []
    supplier_addr_list = []
    winning_amt_list = []

    for winning_talbe in notice_result_table:

        rows_body = winning_talbe.xpath(".//tr//td/text()").getall()

        supplier_name_list.append(rows_body[0] or '')
        supplier_addr_list.append(rows_body[1] or '')
        winning_amt_list.append(str(winning_talbe.xpath(
            ".//tbody//tr//td//span/text()").get()).replace(',', '') or '')

    winning_order_cnt = len(notice_result_table)

    order_id_list = []
    for order_index in range(winning_order_cnt):
        order_id_list.append(str(order_index + 1))
    order_id = ','.join(order_id_list)

    util = Re_Sichuan(text)

    item = {}
    item["project_id"] = util.project_id()
    item["winning_date"] = util.notice_publish_date()
    item["winning_notice_url"] = winning_notice_url
    item["order_id"] = order_id
    item["winning_order_cnt"] = winning_order_cnt  # 中标标项cnt
    item["project_winning_amt"] = winning_amt  # 项目中标总金额
    item["supplier_name"] = ','.join(supplier_name_list)
    item["supplier_addr"] = ','.join(supplier_addr_list)
    item["order_name"] = order_name
    item["winning_amt"] = ','.join(winning_amt_list)
    item["cadidate_name"] = cadidate_name

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

    item["buyer_name"] = util.buyer_name()
    item["buyer_addr"] = util.buyer_addr()
    item["buyer_contact"] = util.buyer_contact()
    item["buyer_phone"] = ''

    item["agency_name"] = util.agent_name()
    item["agency_addr"] = util.agent_addr()
    item["agency_contact"] = util.agency_contact()
    item["agency_phone"] = ''
    # item["text"] = text

    return item
