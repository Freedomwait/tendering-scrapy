
import re
import time
from infoconnect.raw_winning_parser.xian.now import Raw_Result_Parser_Now
from infoconnect.conf.index import keyword_list_all
from infoconnect.raw_winning_parser.xian.old import Raw_Result_Parser_Old
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

name = 'xian'


class sSpider(scrapy.Spider):
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
        'http://www.ccgp-shaanxi.gov.cn/cms-sx/site/shanxi/index.html',
        # ''
    ]

    # 初始化 web driver

    def init_web_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True

        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        self.driver = driver

    def __init__(self):
        super().__init__()
        self.init_web_driver()
        self.url_list = []

    def parse(self, response):
        self.driver.get(
            'http://www.ccgp-shaanxi.gov.cn/freecms/site/shanxi/xxgg/index.html')

        time.sleep(3)
        # 选中结果公告的tab
        menu_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'ul.xxggIndex>li[codes="001021,001022,001023,001024,001025,001026,001029,001006"]')
        menu_btn.click()

        title_input_element = self.driver.find_element(
            By.ID, 'titleName')
        start_time_input_element = self.driver.find_element(
            By.ID, 'stateDate')
        end_time_input_element = self.driver.find_element(
            By.ID, 'endDate')
        start_time_input_element.send_keys("2022-01-01 00:00:00")
        end_time_input_element.send_keys("2023-02-01 23:59:59")

        search_btn = self.driver.find_element(By.ID, 'Inquire')

        # keyword_list_all_test = [
        #     "中控",
        #     "智慧教室",
        #     "教室",
        # ]

        for keyword in keyword_list_all:
            title_input_element.clear()
            title_input_element.send_keys(keyword)
            search_btn.click()
            time.sleep(5)

            # 当前页
            self.parse_current_page()

            # 分页器
            total_page = 1
            current_page = 1
            # 这里有坑，分页器还存在页面上，只是隐藏了
            # 要用数据列表来看
            result_list_elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'ul.noticeListUl>li>a')

            if len(result_list_elements):
                total_page_elements = self.driver.find_elements(
                    By.CSS_SELECTOR, 'li.totalPage')
                # 有数据的情况下必定有分页器
                total_page_element = total_page_elements[1]
                total_page_text = total_page_element.get_attribute("innerHTML")
                total_page_re_result = re.findall(
                    '共&nbsp;(.*?)&nbsp;页', total_page_text)
                if len(total_page_re_result):
                    total_page = int(total_page_re_result[0])
                    # 更多页处理
                    if total_page > 1:
                        while current_page < total_page:
                            current_page += 1
                            total_page_input_element = self.driver.find_element(
                                By.CSS_SELECTOR, 'div#pagination>ul>li.totalPage>input[type="number"]')
                            print(
                                f'total_page, current_page: {total_page} {current_page}')
                            if total_page_input_element:
                                total_page_input_element.clear()
                                total_page_input_element.send_keys(
                                    str(current_page) + Keys.ENTER)
                                time.sleep(5)
                                self.parse_current_page()

        self.driver.close()
        for url in self.url_list:
            yield scrapy.Request(url, callback=self.parse_detail_item)

    # 处理当前页
    def parse_current_page(self):
        result_list_elements = self.driver.find_elements(
            By.CSS_SELECTOR, 'ul.noticeListUl>li>a')

        print('parse_current_page len', len(result_list_elements))
        if result_list_elements and len(result_list_elements):
            for item in result_list_elements:
                detail_url = item.get_attribute('href')
                print(detail_url)
                self.url_list.append(detail_url)

    def parse_detail_item(self, response):

        # old_url_list = [
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be387e22c8ad017f246ed207036e.html?noticeType=001021&noticeId=8a85be387e22c8ad017f246ed207036e
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be347ee720e8017f2a75e5d94818.html?noticeType=001021&noticeId=8a85be347ee720e8017f2a75e5d94818
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be327ee72345017f2f8633a651f3.html?noticeType=001021&noticeId=8a85be327ee72345017f2f8633a651f3
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be347f3fe6d4017f5393e4be56d2.html?noticeType=001021&noticeId=8a85be347f3fe6d4017f5393e4be56d2
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be347f3fe6d4017f53e4dc785d0a.html?noticeType=001021&noticeId=8a85be347f3fe6d4017f53e4dc785d0a
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/2022/8a85be317f7906e9017fd9e31bab0545.html?noticeType=001021&noticeId=7233094f-b0a3-11ec-9a8e-08c0eb20c666
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/2022/8a85be347fe4a76e01801d1912d0324e.html?noticeType=001021&noticeId=28f26dfc-bef3-11ec-9a8e-08c0eb20c666
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/oldweb/8a85be387f91f0bf0180462ab6710032.html?noticeType=001021&noticeId=8a85be387f91f0bf0180462ab6710032
        # http://www.ccgp-shaanxi.gov.cn/freecms/site/shaanxi/ggxx/info/2022/8a85be327fe4aa4701809c30790060c5.html?noticeType=001021&noticeId=3df80637-cf67-11ec-9a8e-08c0eb20c666
        # ]

        if '/oldweb' in response.url:
            raw_data = Raw_Result_Parser_Old(
                response, '//div[@id="print-content"]').export_dict()
        else:
            raw_data = Raw_Result_Parser_Now(
                response, '//div[@id="noticeArea"]').export_dict()

        yield raw_data

    def closed(self, reason):
        print(f'spider xian closed {reason}')
        pass
