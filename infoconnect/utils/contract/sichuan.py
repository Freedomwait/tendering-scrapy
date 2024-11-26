import json
from infoconnect.utils.area.sichuan import SiChuanArea
from infoconnect.utils.index import purchase_type
from infoconnect.utils.nodeparse import NodeParse
from infoconnect.utils.re.sichuan import Re_Sichuan
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from scrapy.selector import Selector


def sichuan_contract_detail(spider, response):
    url = response.url
    resJson = json.loads(response.body)
    if resJson["code"] == "200":
        data_list = resJson["data"]
        if len(data_list):
            current_data = data_list[0]
            html_doc = current_data["content"]
            selector = Selector(text=html_doc).xpath(
                '//div[@class="noticeArea"]')
            text = NodeParse(selector).to_text()

            page_url = current_data["pageurl"]

            util = Re_Sichuan(text)

            item = {}

            item["project_id"] = response.meta["project_id"]
            item["order_id"] = 1
            item["contract_id"] = util.contract_code()
            item['buyer_id'] = 1
            item["contract_amt"] = current_data["budget"]
            item["contract_notice_url"] = 'http://www.ccgp-sichuan.gov.cn' + page_url
            item["contract_cnt"] = 1
            # item["text"] = text

            return item

        else:
            return None
    else:
        return None
