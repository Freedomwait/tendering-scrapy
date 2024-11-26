import time
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class TccloudSpider(scrapy.Spider):
    name = 'tccloud'
    allowed_domains = ['udc.eyar.com',
                       'his.eyar.com']

    custom_settings = {
        "FEEDS": {
            'out/tccloud.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/tccloud.log',
        "LOG_FILE_APPEND": False,
    }

    start_urls = [
        'https://his.eyar.com'
    ]

    def __init__(self):
        super().__init__()
        options = webdriver.ChromeOptions()
        options.headless = False

        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        self.driver = driver
        pass

    def parse(self, response):

        self.driver.get('https://his.eyar.com')
        time.sleep(3)

        # 登录
        username = self.driver.find_element(By.CSS_SELECTOR, '#userName')
        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        loginbtn = self.driver.find_element(By.CSS_SELECTOR, '#loginBtn')

        username.send_keys("jinxiaohua")
        password.send_keys("jinxiaohua520")

        loginbtn.click()

        time.sleep(1)

        self.driver.get(
            'https://his.eyar.com/ops/reception/listHistory.htm?casWebHid=67_480457381717929382')

        time.sleep(5)

        beginDate = self.driver.find_element(By.CSS_SELECTOR, '#beginDate')
        endDate = self.driver.find_element(By.CSS_SELECTOR, '#endDate')
        beginDate.clear()
        beginDate.send_keys('2022-03-24')
        endDate.clear()
        beginDate.send_keys('2023-03-30')

        searchBtn = self.driver.find_element(
            By.CSS_SELECTOR, 'input[value="搜索"]')
        searchBtn.click()

        total = self.driver.find_element(
            By.CSS_SELECTOR, '.purple-button.toPage').get_attribute('data-page')

        print(total)

        for page_index in total:
            page = page_index + 1
            self.parse_page(page)

    def parse_page(self, page=1):
        # page = 1 的默认当前，不用再组装URL

        self.driver.find_element()

        view_btns = self.driver.find_elements(
            By.CSS_SELECTOR, '.gray_btn.mr10[target="_blank"]')
        for view_btn in view_btns:
            link = view_btn.get_attribute('href')

            # scrapy.Reuq

        # 总页数
        self.driver.close()

    def closed(self, reason):
        print(f'spider tccloud closed {reason}')
        pass
