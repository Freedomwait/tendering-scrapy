
import time
from infoconnect.utils.nodeparse import NodeParse
from infoconnect.utils.re.henan import Re_Henan
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class sSpider(scrapy.Spider):
    name = 's'
    allowed_domains = ['zfcgmanager.czt.zj.gov.cn',
                       'www.ccgp-beijing.gov.cn', 'hngp.gov.cn']

    custom_settings = {
        "FEEDS": {
            'out/s.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/s.log',
        "LOG_FILE_APPEND": False,
    }

    start_urls = [
        'http://www.ccgp-beijing.gov.cn'
    ]

    def __init__(self):
        super().__init__()

        d = {
            'project_id': [],
            'winning_date': [],
            'winning_notice_url': [],
            'order_id': [],
            'winning_order_cnt': [],
            'project_winning_amt': [],
            'supplier_name': [],
            'supplier_addr': [],
            "order_name": [],
            "winning_amt": [],
            "cadidate_name": [],
            "buyer_name": [],
            "buyer_addr": [],
            "buyer_contact": [],
            "buyer_phone": [],
            "agency_name": [],
            "agency_addr": [],
            "agency_contact": [],
            "agency_phone": []
        }
        self.result_df = pd.DataFrame(data=d)

        pass

    def parse(self, response):

        options = webdriver.ChromeOptions()
        # options.headless = True

        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

        # df = pd.read_csv(
        #     f'input/henangovwinningnotices.csv').dropna(axis=0, subset=[
        #         '标题'], how='any')

        # title_list = df["标题"].tolist()

        title_list = [
            "洛阳职业技术学院信创电子教室与实训平台项目-中标公告",
            "清丰县春晖路小学教学办公设备购置-中标公告"
        ]

        for title in title_list:
            driver.get('http://hngp.gov.cn/')
            time.sleep(1)

            SearchInput = driver.find_element(
                By.CSS_SELECTOR, 'input[name="q"]')
            btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

            SearchInput.send_keys(title)
            btn.click()

            time.sleep(3)

            result_text = driver.find_element(By.CSS_SELECTOR, '.Title02').text

            result_url_list = []

            if result_text == '搜索结果：您共搜到0条内容':
                self.logger.info(f'标题未搜索到结果')
            else:
                result_list = driver.find_element(
                    By.CSS_SELECTOR, '.List2>ul>li>a')
                print('result_list')
                print(result_list)
                if result_list:
                    result_url = result_list.get_attribute('href')
                    result_url_list.append(result_url)
                    result_list.click()

                    time.sleep(5)
                    main_content = driver.find_element(By.ID, 'print-content')
                    print('main_content innerHTML')

                    doc_html = main_content.get_attribute('innerHTML')

                    self.parese_item(doc_html, result_url)

                    print('to home page again')

                    driver.get('http://hngp.gov.cn')
                    time.sleep(1)

        self.logger.info('before close')
        self.result_df.to_csv('out/s.csv')
        driver.close()

    def parese_item(self, doc_html, url):
        main_content = Selector(text=doc_html).xpath('//div[@id="content"]')
        text = NodeParse(main_content).to_text()

        util = Re_Henan(text)

        projectCode = util.project_id()
        noticePubDate = util.publish_date()
        winning_notice_url = url
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

        # TODO 供应商中标信息有的是表格形式
        # http://www.ccgp-beijing.gov.cn/xxgg/qjzfcggg/qjzbjggg/t20220316_1412985.html
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

        self.result_df.loc[len(self.result_df)] = [
            projectCode,
            noticePubDate,
            winning_notice_url,
            order_id,
            winning_order_cnt,
            project_winning_amt,
            supplier_name,
            supplier_addr,
            order_name,
            winning_amt,
            cadidate_name,
            util.buyer_name(),
            util.buyer_addr(),
            util.buyer_contact(),
            util.buyer_phone(),
            util.agent_name(),
            util.agent_addr(),
            util.agent_contact(),
            util.agent_phone()
        ]

        # return item

    def closed(self, reason):
        print(f'spider detail closed {reason}')
        pass
