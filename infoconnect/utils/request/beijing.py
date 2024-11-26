import json
from infoconnect.utils.area.sichuan import SiChuanArea
from infoconnect.utils.index import purchase_type
from infoconnect.utils.nodeparse import NodeParse
from infoconnect.utils.re.sichuan import Re_Sichuan
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from scrapy.selector import Selector


def beijing_request_detail(spider, response):
    html_doc_string = response.body.decode('utf-8')
    # spider.logger.debug('html_doc_string')
    # spider.logger.debug(html_doc_string)

    # 这里对查询到的结果过滤，只保留中标公告
    result_link_list = Selector(text=html_doc_string).xpath(
        '//a[@class="searchresulttitle"]')

    print(response)
    print(f'beijing_request_detail result_link_list: {result_link_list}')

    return None

    # for item in result_link_list:
    #     title_text = node_text(item)
    #     title_link = item.xpath("./@href").get()
    #     result_title = re.findall('中标公告$', title_text)
    #     if len(result_title):
    #         result_url_list.append(title_link)
    # url = response.url
    # resJson = json.loads(response.body)

    # spider.logger.info(f'parse beijing request data from url: {url}')
    # spider.logger.info(f'resJson: {resJson}')
    # if resJson["code"] == "200":
    #     data_list = resJson["data"]
    #     if len(data_list):
    #         current_data = data_list[0]
    #         html_doc = current_data["content"]
    #         selector = Selector(text=html_doc).xpath('//div[@id="noticeArea"]')
    #         text = NodeParse(selector).to_text()

    #         util = Re_Sichuan(text)

    #         # 类型，优先从标题判断，如果没有再从页面匹配
    #         sourcing_type = util.sourcing_type()

    #         # 地区 code
    #         regionCode = current_data["regionCode"]

    #         sichuanArea = SiChuanArea().get_areainfo_by_value(regionCode)

    #         order_count = 1
    #         page_url = current_data["pageurl"]

    #         item = {}

    #         item["project_id"] = response.meta["project_id"]
    #         item["project_name"] = util.project_name_race()
    #         item['sourcing_type'] = sourcing_type

    #         buyer_id = 1
    #         buyer_count = 1

    #         item['province'] = sichuanArea['province']
    #         item['county'] = sichuanArea['county']
    #         item['district'] = sichuanArea['district']

    #         item['agency_name'] = current_data["agency"]
    #         item['agency_addr'] = util.bidding_agent_purchaser_address()
    #         item['agency_contact'] = util.bidding_agent_purchaser_person()
    #         item['agency_phone'] = util.bidding_agent_purchaser_contact()

    #         item['request_date'] = current_data["noticeTime"]
    #         item['closing_date'] = util.purchase_dead_line()

    #         item['order_count'] = order_count
    #         item['buyer_count'] = buyer_count

    #         item["project_max_amt"] = util.maximum_price()
    #         item["request_notice_url"] = 'http://www.ccgp-sichuan.gov.cn' + page_url
    #         item["budget_amt"] = current_data["budget"]
    #         item["buyer_id"] = buyer_id
    #         item["buyer_name"] = current_data["purchaser"]
    #         item["buyer_addr"] = current_data["purchaserAddr"]
    #         item["buyer_contact"] = util.buyer_contact()
    #         item["buyer_phone"] = current_data["purchaserLinkPhone"]
    #         item["source_id"] = response.meta["source_id"]
    #         # item["text"] = text

    #         return item

    #     else:
    #         spider.logger.debug(
    #             f'sichuan request get none item from project code: {response.meta["project_id"]}')
    #         return None
    # else:
    #     return None
