
import re
from urllib.parse import parse_qs, urlparse
from infoconnect.utils.index import parse_table, parse_table_with_header
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.re.bj import Re_bj
from infoconnect.utils.re.hebei import Re_hebei
from infoconnect.utils.re.henan import Re_Henan
from infoconnect.utils.re.sichuan import Re_Sichuan
import scrapy
from scrapy.selector import Selector


class NoticeSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.hngp.gov.cn']

    start_urls = [
        # 'http://www.ccgp-beijing.gov.cn/xxgg/qjzfcggg/qjzbjggg/t20220316_1412985.html',  # 表格中
        # 多个标项
        # 'http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbjggg/t20220519_1427463.html',

        # 'http://www.ccgp-sichuan.gov.cn/freecms/site/sichuan/ggxx/info/2023/8a69c260858272080185957a5a131391.html?noticeType=00102'
        # 'http://www.ccgp-sichuan.gov.cn/freecms/site/sichuan/ggxx/info/2023/8a69c85a8563bb1f01857c0b4d8803ff.html'
        # 'http://www.ccgp-sichuan.gov.cn/freecms/site/sichuan/ggxx/info/2023/8a69c260858272080185957a5a131391.html?noticeType=00102'
        # 多个包
        # 'http://www.ccgp-sichuan.gov.cn/freecms/site/sichuan/ggxx/info/2022/8a69c6c4853037b701853936bda12e3a.html'

        # 'http://localhost:8050/render.html?url=http://www.ccgp-hebei.gov.cn/hd/hd_ca/cggg/zhbggAAAA/202207/t20220729_1645334.html'
        # 'http://www.ccgp-hebei.gov.cn/qhd/qhd_bdh/cggg/zhbggAAAA/202201/t20220124_1539481.html'
        # 'http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbjggg/t20230106_1478357.html'
        # 'http://hngp.gov.cn/henan/content?infoId=1266613&channelCode=H640102',
        # 多个包
        'http://hngp.gov.cn/henan/content?infoId=1152564&channelCode=H680202'
    ]

    custom_settings = {
        "FEEDS": {
            f'out/test.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/test.log',
        "LOG_FILE_APPEND": False
    }

    def parse(self, response):

        # 渲染出来的网页是动态生成的，找到实际请求的地址
        doc_html = response.body
        # main_content = Selector(text=doc_html).xpath('//div[@id="content"]')

        scripts = Selector(text=doc_html).xpath('//script').getall()
        script_string = scripts[1]

        real_url = re.findall('\$\.get\(\"(.*?)\", function', script_string)
        if len(real_url):

            detail_url = 'http://www.hngp.gov.cn' + real_url[0]
            print(f'detail_url: {detail_url}')

            yield scrapy.Request(detail_url, meta={"page_url": response.url}, callback=self.parse_detail)

    def parse_detail(self, response):
        doc_html = response.body
        main_content = Selector(text=doc_html).xpath(
            '//table[@class="Content"]')

        text = NodeParse(main_content).to_text()

        util = Re_Henan(text)

        projectCode = util.project_id()
        noticePubDate = util.publish_date()
        winning_notice_url = response.url
        project_winning_amt = ''
        order_id = 1
        winning_order_cnt = 1
        supplier_name = ''
        supplier_addr = ''
        order_name = util.project_name()
        winning_amt = ''
        cadidate_name = ''

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
        item["buyer_contact"] = util.buyer_contact()
        item["buyer_phone"] = util.buyer_phone()

        item["agency_name"] = util.agent_name()
        item["agency_addr"] = util.agent_addr()
        item["agency_contact"] = util.agent_contact()
        item["agency_phone"] = util.agent_phone()
        item["text"] = text

        yield item
