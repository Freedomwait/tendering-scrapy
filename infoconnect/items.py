# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 中标结果公告


class WinningNoticeItem(scrapy.Item):
    project_id = scrapy.Field()
    order_id = scrapy.Field()
    winning_date = scrapy.Field()
    winning_order_cnt = scrapy.Field()
    project_winning_amt = scrapy.Field()
    winning_notice_url = scrapy.Field()
    supplier_name = scrapy.Field()
    supplier_addr = scrapy.Field()
    order_name = scrapy.Field()
    winning_amt = scrapy.Field()
    cadidate_name = scrapy.Field()
    # 通用
    source = scrapy.Field()
    keyword = scrapy.Field()
    text = scrapy.Field()
    pass

# 合同公告


class ContractNoticeItem(scrapy.Item):
    project_id = scrapy.Field()
    order_id = scrapy.Field()
    contract_id = scrapy.Field()
    buyer_id = scrapy.Field()
    contract_amt = scrapy.Field()
    contract_notice_url = scrapy.Field()
    contract_cnt = scrapy.Field()
    # 通用
    source = scrapy.Field()
    keyword = scrapy.Field()
    text = scrapy.Field()
    pass


class RequestNotiecItem(scrapy.Item):
    project_id = scrapy.Field()
    project_name = scrapy.Field()
    sourcing_type = scrapy.Field()
    province = scrapy.Field()
    county = scrapy.Field()
    district = scrapy.Field()
    agency_name = scrapy.Field()
    agency_addr = scrapy.Field()
    agency_contact = scrapy.Field()
    agency_phone = scrapy.Field()
    request_date = scrapy.Field()
    closing_date = scrapy.Field()
    order_count = scrapy.Field()
    buyer_count = scrapy.Field()
    project_max_amt = scrapy.Field()
    request_notice_url = scrapy.Field()
    budget_amt = scrapy.Field()
    buyer_id = scrapy.Field()
    buyer_name = scrapy.Field()
    buyer_addr = scrapy.Field()
    buyer_contact = scrapy.Field()
    buyer_phone = scrapy.Field()
    source_id = scrapy.Field()
    # 通用
    source = scrapy.Field()
    keyword = scrapy.Field()
    text = scrapy.Field()
    pass
