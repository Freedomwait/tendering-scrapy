import re
import pandas as pd
from infoconnect.raw_winning_parser.xian.now import Raw_Result_Parser_Now
from infoconnect.raw_winning_parser.xian.old import Raw_Result_Parser_Old
import scrapy
from scrapy.selector import Selector
from infoconnect.utils.nodeparse import NodeParse


name = 'xian_test'


class TestXianSpider(scrapy.Spider):
    name = name
    allowed_domains = ['www.ccgp-shaanxi.gov.cn']

    custom_settings = {
        "FEEDS": {
            f'out/{name}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/{name}.log',
        "LOG_FILE_APPEND": False,
    }

    start_urls = [
        # 正常单个标
        # 'http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/2022/8a69c9da852dc10a018561177aa709a5.html',
        # 废标
        # 'http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/2022/8a69c86f852dbe9b01855144bbcd4443.html?noticeType=001006&noticeId=329ebcb9-85b2-11ed-9a8e-08c0eb20c666',
        # 多标
        # 'http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/2022/8a69c4c88405ac2f01846499af173a13.html?noticeType=001021&noticeId=348cf459-6170-11ed-9a8e-08c0eb20c666'
        # ccpg
        # 'http://www.ccgp.gov.cn/cggg/zygg/zbgg/202207/t20220705_18201687.htm'
        # 老版本
        #
        # 'http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be387e22c8ad017f246ed207036e.html?noticeType=001021&noticeId=8a85be387e22c8ad017f246ed207036e'
        # 'http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be347f3fe6d4017f53e4dc785d0a.html?noticeType=001021&noticeId=8a85be347f3fe6d4017f53e4dc785d0a'
        # 'http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/2022/8a69c59682a320a40182b3cd4ece29b3.html?noticeType=001021&noticeId=e86e9aa5-1f64-11ed-9a8e-08c0eb20c666'
        'http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be347ee720e8017f2a75e5d94818.html?noticeType=001021&noticeId=8a85be347ee720e8017f2a75e5d94818'
    ]

    def __init__(self):
        super().__init__()
        pass

    def parse(self, response):
        # xpath = '//div[@class="vF_detail_content"]'
        # xpath = '//div[@id="print-content"]'
        # raw_data = Raw_Result_Parser_Old(
        # response, xpath).export_dict()

        if '/oldweb' in response.url:
            raw_data = Raw_Result_Parser_Old(
                response, '//div[@id="print-content"]').export_dict()
        else:
            raw_data = Raw_Result_Parser_Now(
                response, '//div[@id="noticeArea"]').export_dict()

        # yield raw_data

        print(raw_data)
        yield raw_data

    def closed(self, reason):
        print(f'spider {name} closed {reason}')
        pass
