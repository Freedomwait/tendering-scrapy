
import scrapy
import pandas as pd
from infoconnect.raw_winning_parser.xian.bzz1 import Raw_Result_Parser_Bzz1
from infoconnect.raw_winning_parser.xian.bzz2 import Raw_Result_Parser_Bzz2

name = 'xian_bzz'


class XianBzzSpider(scrapy.Spider):
    name = name
    allowed_domains = ['www.ccgp-shaanxi.gov.cn', 'www.ccgp.gov.cn']

    custom_settings = {
        "FEEDS": {
            f'out/{name}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/{name}.log',
        "LOG_FILE_APPEND": False,
    }

    start_urls = [
        'http://www.ccgp-shaanxi.gov.cn/cms-sx/site/shanxi/index.html',
    ]

    def __init__(self):
        # self.url_list = pd.read_csv('out/bzz_xian.csv')['原文链接'].tolist()
        # print(self.url_list)

        self.url_list1 = [
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202208/t20220816_18471005.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202212/t20221214_19230995.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202212/t20221216_19248093.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202212/t20221223_19287081.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202212/t20221224_19290969.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202209/t20220913_18641505.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202209/t20220907_18612548.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202211/t20221102_18934502.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202208/t20220826_18532446.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202210/t20221021_18864896.htm",
        ]

        self.url_list2 = [
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202206/t20220630_18174283.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202207/t20220705_18201687.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202207/t20220715_18273617.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202301/t20230109_19354505.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202212/t20221202_19138798.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202206/t20220610_18056703.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202212/t20221207_19173130.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202202/t20220218_17603944.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202209/t20220907_18608768.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202204/t20220414_17771669.htm",
            "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202207/t20220707_18218366.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202207/t20220720_18301825.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202207/t20220706_18210192.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202207/t20220715_18274462.htm",
            "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202209/t20220913_18642014.htm",
        ]

    def parse(self, response):
        for url in self.url_list1:
            yield scrapy.Request(url, callback=self.parse_detail_item)

        for url in self.url_list2:
            yield scrapy.Request(url, callback=self.parse_detail_item2)

    def parse_detail_item(self, response):
        raw_data = Raw_Result_Parser_Bzz1(
            response, '//div[@class="vF_detail_content"]').export_dict()

        yield raw_data

    def parse_detail_item2(self, response):
        raw_data = Raw_Result_Parser_Bzz2(
            response, '//div[@class="vF_detail_content"]').export_dict()

        yield raw_data

    def closed(self, reason):
        print(f'spider bzz_xian closed {reason}')
        pass
