import json
from infoconnect.utils.area.sichuan import SiChuanArea
from infoconnect.utils.index import purchase_type
from infoconnect.utils.nodeparse import NodeParse
from infoconnect.utils.re.sichuan import Re_Sichuan
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from scrapy.selector import Selector


def shanghai_contract_detail(spider, response):
    item = {}

    item["project_id"] = response.meta["project_id"]
    item["order_id"] = 1
    item["contract_id"] = ''
    item['buyer_id'] = 1
    item["contract_amt"] = ''
    item["contract_notice_url"] = response.url
    item["contract_cnt"] = 1
    # item["text"] = text

    return item
