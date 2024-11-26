import json
from infoconnect.utils.area.shanghai import ShangHaiArea
from infoconnect.utils.re.shanghai import Re_Shanghai
from scrapy.selector import Selector
from infoconnect.utils.re.zhejiang import Re_Zhejiang
from infoconnect.utils.re.sichuan import Re_Sichuan
from infoconnect.utils.nodeparse import NodeParse
from infoconnect.utils.index import purchase_type
from infoconnect.utils.area.sichuan import SiChuanArea


def shanghai_request_detail(spider, response):

    html_doc = response.body.decode('utf-8')
    # selector = Selector(text=html_doc).xpath('//body')
    detailJsonData = Selector(text=html_doc).xpath(
        '//input[@name="articleDetail"]/@value').get()

    detail_json = json.loads(detailJsonData)

    content = detail_json["content"]

    main_content = Selector(text=content).xpath(
        '//body')

    text = NodeParse(main_content).to_text()
    spider.logger.info('shanghai_request text')
    spider.logger.info(text)
    util = Re_Shanghai(text)

    # spider.logger.info('shanghai_result_detail')
    # spider.logger.info(detail_json)

    # project_name = detail_json["projectName"]
    # if project_name == '':
    project_name = util.project_name()
    item = {}
    item["project_id"] = response.meta["project_id"]
    item["project_name"] = project_name
    item['sourcing_type'] = response.meta["procurementMethod"]

    buyer_id = 1
    buyer_count = 1
    order_count = 1

    order_packages = util.order_packages()

    districtCode = detail_json["districtCode"]
    shanghai_area = ShangHaiArea().get_areainfo_by_value(districtCode)

    item['province'] = shanghai_area['province']
    item['county'] = shanghai_area['county']
    item['district'] = shanghai_area['district']

    item['agency_name'] = util.bidding_agent_name()
    item['agency_addr'] = util.bidding_agent_purchaser_address()
    item['agency_contact'] = util.bidding_agent_purchaser_person()
    item['agency_phone'] = util.bidding_agent_purchaser_contact()

    item['request_date'] = detail_json["publishDate"]
    item['closing_date'] = util.purchase_dead_line()

    item['order_count'] = len(order_packages)
    item['buyer_count'] = buyer_count

    item["project_max_amt"] = util.max_amt()
    item["request_notice_url"] = response.url
    item["budget_amt"] = util.budget_account()
    item["buyer_id"] = buyer_id
    item["buyer_name"] = util.buyer_name()
    item["buyer_addr"] = util.buyer_addr()
    item["buyer_contact"] = util.buyer_contact()
    item["buyer_phone"] = util.buyer_phone()
    item["source_id"] = response.meta["source_id"]
    # item["text"] = text

    return item
