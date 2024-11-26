import re
import pandas as pd
from infoconnect.conf.index import PLACE_MAP
from infoconnect.utils.detail.anhui import anhui_result_detail
from infoconnect.utils.re.hubei import Re_Hubei
import scrapy
from scrapy.selector import Selector
from infoconnect.utils.re.ccgp import Re_Ccgp
from infoconnect.utils.nodeparse import NodeParse


name = 'test_hubei'
home_page = 'http://www.ccgp-hubei.gov.cn/notice/202204/notice_2439e40e1e674eaf945d12eba2b47d5d.html'


class TestHubeiSpider(scrapy.Spider):
    name = name
    allowed_domains = ['www.ccgp-hubei.gov.cn']

    custom_settings = {
        "FEEDS": {
            f'out/{name}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/{name}.log',
        "LOG_FILE_APPEND": False,
    }

    start_urls = [
        home_page
    ]

    def __init__(self):
        super().__init__()

        # 读取所有的 ccgp 链接，包含地区地址，然后融合作为输入
        # list = {
        #     PLACE_MAP["ZHEJIANG"]: 'input/more/zhejiang.xlsx',
        #     PLACE_MAP["BEIJING"]: 'input/more/beijing.xlsx',
        #     PLACE_MAP["HENAN"]: 'input/more/henan.xlsx',
        #     PLACE_MAP["ANHUI"]: 'input/more/anhui.xlsx',
        #     PLACE_MAP["SICHUAN"]: 'input/more/sichuan.xlsx',
        #     PLACE_MAP["HUBEI"]: 'input/more/hubei.xlsx',
        #     PLACE_MAP["SHANGHAI"]: 'input/more/shanghai.xlsx',
        # }

        # self.result_df = pd.DataFrame(data={
        #     'source_id': [],
        #     'url': [],
        # })

        pass

    # def parse(self, response):

    #     df = pd.read_excel(
    #         'input/more/hubei.xlsx').dropna(axis=0, subset=[
    #             '原文链接'], how='any')

    #     urls = df["原文链接"].tolist()
    #     for url in urls:
    #         if 'http://www.ccgp-hubei.gov.cn' in url:
    #             yield scrapy.Request(url, meta={"source_id": "5"}, callback=self.parse_item)

    def parse(self, response):
        doc_html = response.body.decode('utf-8')
        main_content = Selector(text=doc_html).xpath(
            '//div[@class="art_con"]')
        text = NodeParse(main_content).to_text()

        print(f'text: {text}')

        util = Re_Hubei(text)
        pubTime = util.pub_date()
        project_code = util.project_code()
        order_name = util.order_name()

        projectCode = project_code
        noticePubDate = pubTime
        winning_notice_url = response.url
        project_winning_amt = ''
        order_id = 1
        winning_order_cnt = 1
        supplier_name = util.supplier_name()
        supplier_addr = util.supplier_addr()
        order_name = order_name
        winning_amt = util.winning_amt()
        cadidate_name = ''

        buyer_contact = util.buyer_contact()
        agent_contact = util.agent_contact()

        item = {}
        item["project_id"] = projectCode
        item["winning_date"] = noticePubDate
        item["winning_notice_url"] = winning_notice_url
        item["order_id"] = order_id
        item["winning_order_cnt"] = winning_order_cnt  # 中标标项cnt
        item["project_winning_amt"] = project_winning_amt  # 项目中标总金额

        item["supplier_name"] = supplier_name
        item["supplier_addr"] = supplier_addr
        item["order_name"] = order_name
        item["winning_amt"] = winning_amt
        item["cadidate_name"] = cadidate_name

        item["buyer_name"] = util.buyer_name()
        item["buyer_addr"] = util.buyer_addr()
        item["buyer_contact"] = ''
        item["buyer_phone"] = buyer_contact

        item["agency_name"] = util.agent_name()
        item["agency_addr"] = util.agent_addr()
        item["agency_contact"] = ''
        item["agency_phone"] = agent_contact
        item["source_id"] = '5'
        item["text"] = text

        yield item

    def closed(self, reason):
        print(f'spider {name} closed {reason}')
        pass
