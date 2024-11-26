import re
import pandas as pd
from infoconnect.conf.index import PLACE_MAP
from infoconnect.utils.detail.anhui import anhui_result_detail
from infoconnect.utils.re.bj import Re_bj
from infoconnect.utils.re.ccgp_beijing import Re_Ccgp_Beijing
from infoconnect.utils.re.hubei import Re_Hubei
import scrapy
from scrapy.selector import Selector
from infoconnect.utils.re.ccgp import Re_Ccgp
from infoconnect.utils.nodeparse import NodeParse


home_page = 'http://www.ccgp.gov.cn/cggg/zygg/zbgg/202212/t20221216_19248478.htm'
name = 'ccgp_beijing'


class CcgpSpider(scrapy.Spider):
    name = name
    allowed_domains = ['www.ccgp.gov.cn']

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
        list = {
            # PLACE_MAP["ZHEJIANG"]: 'input/more/zhejiang.xlsx',
            PLACE_MAP["BEIJING"]: 'input/more/beijing1.csv',
            # PLACE_MAP["HENAN"]: 'input/more/henan.xlsx',
            # PLACE_MAP["ANHUI"]: 'input/more/anhui.xlsx',
            # PLACE_MAP["SICHUAN"]: 'input/more/sichuan.xlsx',
            # PLACE_MAP["HUBEI"]: 'input/more/hubei.xlsx',
            # PLACE_MAP["SHANGHAI"]: 'input/more/shanghai.xlsx',
        }

        self.result_df = pd.DataFrame(data={
            'source_id': [],
            'url': [],
        })

        for key, value in list.items():
            df = pd.read_csv(
                value).dropna(axis=0, subset=[
                    '原文链接'], how='any')

            urls = df["原文链接"].tolist()
            for url in urls:
                # url_list.append(url)
                # source_id_list.append(key)
                if 'http://www.ccgp.gov.cn/cggg' in url:
                    self.result_df.loc[len(self.result_df)] = [key, url]
        pass

    def parse(self, response):

        self.result_df.to_csv('input/more/ccgp.csv')

        print(f'行数： {self.result_df.shape[0]}')

        zy_count = 0
        df_count = 0
        other_count = 0

        for index, rows in self.result_df.iterrows():
            url = rows["url"]
            source_id = rows["source_id"]

            if 'http://www.ccgp.gov.cn/cggg/dfgg' in url:
                # 地方公告由地方各自的模版解析
                # print(f'地方公告: {url}')
                df_count += 1
                # if source_id == PLACE_MAP["ANHUI"]:
                yield scrapy.Request(url, meta={"source_id": source_id}, callback=self.parse_beijing_item)
                # else:
                print('need to do')
            # else:
            #     print(f'非 ccpg 公告: {url}')
            elif 'http://www.ccgp.gov.cn/cggg/zygg' in url:
                print(f'中央公告: {url}')
                zy_count += 1
                # 分为地方和中央公告
                yield scrapy.Request(url, meta={"source_id": source_id}, callback=self.parese_zy_item)
            # else:
            #     print(f'其他类型公告: {url}')
            #     other_count += 1

        print(f'中央，地方，其他： {df_count}, {df_count}, {other_count}')

    def parese_zy_item(self, response):
        doc_html = response.body.decode('utf-8')
        main_content = Selector(text=doc_html).xpath(
            '//div[@class="vF_deail_maincontent"]')
        text = NodeParse(main_content).to_text()

        pubTime = Selector(text=doc_html).xpath(
            '//span[@id="pubTime"]/text()').get()

        util = Re_Ccgp(text)

        projectCode = util.project_id()
        noticePubDate = pubTime
        winning_notice_url = response.url
        project_winning_amt = ''
        order_id = 1
        winning_order_cnt = 1
        supplier_name = util.supplier_name()
        supplier_addr = util.supplier_addr()
        order_name = util.project_name()
        winning_amt = util.winning_amt_zy()
        cadidate_name = ''

        buyer_contact = util.buyer_contact()

        agent_contact = util.agent_contact()

        winning_order_cnt = len(supplier_name)

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
        item["buyer_contact"] = buyer_contact
        item["buyer_phone"] = ''

        item["agency_name"] = util.agent_name()
        item["agency_addr"] = util.agent_addr()
        item["agency_contact"] = agent_contact
        item["agency_phone"] = ''
        item["source_id"] = response.meta["source_id"]
        # item["text"] = text

        yield item

    def parese_df_item(self, response):
        source_id = response.meta["source_id"]

        result_item = {}

        # if source_id == PLACE_MAP["ANHUI"]:

        #     print(f'anhui item url: {response.url}')
        #     result_item = self.parse_anhui_item(response)

        #     yield result_item
        if source_id == PLACE_MAP["HUBEI"]:

            print(f'parse_hubei_item url: {response.url}')
            result_item = self.parse_hubei_item(response)

            yield result_item
        # if source_id == PLACE_MAP["HEBEI"]:

        #     print(f'anhui item url: {response.url}')
        #     result_item = self.parse_hubei_item(response)

        #     yield result_item

        # if source_id == PLACE_MAP["SHNANGHAI"]:

        #     print(f'anhui item url: {response.url}')
        #     result_item = self.parse_hubei_item(response)

        #     yield result_item
        # if source_id == PLACE_MAP["ZHEJIANG"]:

        #     print(f'anhui item url: {response.url}')
        #     result_item = self.parse_hubei_item(response)

        #     yield result_item

        # if source_id == PLACE_MAP["HENAN"]:

        #     print(f'anhui item url: {response.url}')
        #     result_item = self.parse_hubei_item(response)

        #     yield result_item

    def parse_anhui_item(self, response):

        doc_html = response.body.decode('utf-8')
        main_content = Selector(text=doc_html).xpath(
            '//div[@class="vF_deail_maincontent"]')
        text = NodeParse(main_content).to_text()
        doc_html = response.body.decode('utf-8')
        main_content = Selector(text=doc_html).xpath(
            '//div[@class="vF_deail_maincontent"]')
        text = NodeParse(main_content).to_text()

        pubTime = Selector(text=doc_html).xpath(
            '//span[@id="pubTime"]/text()').get()

        util = Re_Ccgp(text)

        project_id = util.project_id()
        if len(project_id) == 0:
            project_id = re.findall('项目编号：(.*?)二、项目名称', text)
        if len(project_id) == 0:
            project_id = re.findall('项目编号:(.*?)二、项目名称', text)

        order_name = util.project_name()
        if len(order_name) == 0:
            order_name = re.findall('项目名称:(.*?)三、中标（成交）信息', text)

        print(project_id)
        print(type(project_id))

        projectCode = project_id
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

        winning_order_cnt = len(supplier_name)

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
        item["buyer_contact"] = buyer_contact
        item["buyer_phone"] = ''

        item["agency_name"] = util.agent_name()
        item["agency_addr"] = util.agent_addr()
        item["agency_contact"] = agent_contact
        item["agency_phone"] = ''
        item["source_id"] = response.meta["source_id"]
        # item["text"] = text

        return item

    def parse_zhejiang_item(self, response):

        return {}

    def parse_beijing_item(self, response):

        doc_html = response.body.decode('utf-8')
        main_content = Selector(text=doc_html).xpath(
            '//div[@class="vF_deail_maincontent"]')
        text = NodeParse(main_content).to_text()

        pubTime = Selector(text=doc_html).xpath(
            '//span[@id="pubTime"]/text()').get()

        util = Re_Ccgp_Beijing(text)

        projectCode = util.project_id()
        noticePubDate = pubTime
        winning_notice_url = response.url
        project_winning_amt = ''
        order_id = 1
        winning_order_cnt = 1
        supplier_name = util.supplier_name()
        supplier_addr = util.supplier_addr()
        order_name = util.project_name()
        winning_amt = util.winning_amt()
        cadidate_name = ''

        buyer_contact = util.buyer_contact()

        agent_contact = util.agent_contact()

        winning_order_cnt = len(supplier_name)

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
        item["buyer_contact"] = buyer_contact
        item["buyer_phone"] = ''

        item["agency_name"] = util.agent_name()
        item["agency_addr"] = util.agent_addr()
        item["agency_contact"] = agent_contact
        item["agency_phone"] = ''
        item["source_id"] = response.meta["source_id"]
        # item["text"] = text

        yield item

    def parse_henan_item(self, response):

        return {}

    def parse_hebei_item(self, response):

        return {}

    def parse_shanghai_item(self, response):
        doc_html = response.body.decode('utf-8')
        main_content = Selector(text=doc_html).xpath(
            '//div[@class="vF_deail_maincontent"]')
        text = NodeParse(main_content).to_text()

        pubTime = Selector(text=doc_html).xpath(
            '//span[@id="pubTime"]/text()').get()

        util = Re_Ccgp(text)

        projectCode = util.project_id()
        noticePubDate = pubTime
        winning_notice_url = response.url
        project_winning_amt = ''
        order_id = 1
        winning_order_cnt = 1
        supplier_name = util.supplier_name()
        supplier_addr = util.supplier_addr()
        order_name = util.project_name()
        winning_amt = util.winning_amt_zy()
        cadidate_name = ''

        buyer_contact = util.buyer_contact()

        agent_contact = util.agent_contact()

        winning_order_cnt = len(supplier_name)

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
        item["buyer_contact"] = buyer_contact
        item["buyer_phone"] = ''

        item["agency_name"] = util.agent_name()
        item["agency_addr"] = util.agent_addr()
        item["agency_contact"] = agent_contact
        item["agency_phone"] = ''
        item["source_id"] = response.meta["source_id"]

        return item

    def closed(self, reason):
        print(f'spider {name} closed {reason}')
        pass
