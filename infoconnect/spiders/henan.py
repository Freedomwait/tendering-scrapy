
import time
from infoconnect.utils.nodeparse import NodeParse
from infoconnect.utils.re.henan import Re_Henan
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

name = 'henan'


class sSpider(scrapy.Spider):
    name = name
    allowed_domains = ['zfcgmanager.czt.zj.gov.cn',
                       'www.ccgp-beijing.gov.cn', 'hngp.gov.cn']

    custom_settings = {
        "FEEDS": {
            f'out/{name}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/{name}.log',
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

        df = pd.read_csv(
            f'input/henangovwinningnotices.csv').dropna(axis=0, subset=[
                '标题'], how='any')

        print(f'行数： {df.shape[0]}')

        title_list = df["标题"].tolist()

        # title_list = [
        #     "洛阳职业技术学院信创电子教室与实训平台项目-中标公告",
        #     "清丰县春晖路小学教学办公设备购置-中标公告",
        #     "获嘉县职业中等专业学校双高三期项目-中标公告"
        # "三门峡职业技术学院建筑工程学院力学与结构协同创新研究中心建设项目-中标公告"
        # ]

        for title in title_list:
            driver.get('http://hngp.gov.cn/')
            time.sleep(1)

            # 叉掉广告，以免干扰后面的输入
            # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <a class="adClose">...</a> is not clickable at point (883, 211).
            # close_ad_btns = driver.find_elements(By.CLASS_NAME,
            #                                      'adClose')

            # close_ad_btns = WebDriverWait(driver, timeout=3).until(
            #     lambda d: d.find_elements(By.CLASS_NAME, "adClose"))

            # for btn in close_ad_btns:
            #     # try {
            #     # btn.click()
            #     # } catch(Exception e) {
            #     # new Actions(getWebDriver()).sendKeys(Keys.PAGE_DOWN).perform();
            #     # element.click();
            #     # ActionChains(driver).click(btn).perform()

            #     btn.click()
            #     # }

            SearchInput = driver.find_element(
                By.CSS_SELECTOR, 'input[name="q"]')
            # btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

            SearchInput.send_keys(title + Keys.ENTER)

            # btn.click()

            time.sleep(3)

            result_text = ''
            result_ele = driver.find_element(By.CSS_SELECTOR, '.Title02')
            if result_ele:
                result_text = result_ele.text

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

                    print(f'result_url: {result_url}')
                    result_url_list.append(result_url)
                    result_list.click()

                    time.sleep(2)
                    main_content = driver.find_element(By.ID, 'print-content')
                    print('main_content innerHTML')

                    doc_html = main_content.get_attribute('innerHTML')

                    self.parese_item(doc_html, result_url)

                    print('to home page again')

                    driver.get('http://www.hngp.gov.cn/henan')
                    time.sleep(2)

        self.logger.info('before close')
        self.result_df.to_csv(f'out/{name}.csv')
        driver.close()

    def parese_item(self, doc_html, url):
        if (doc_html):

            main_content = Selector(text=doc_html).xpath(
                '//table[@class="Content"]')
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

            # 一条的时候
            target_trs = Selector(text=doc_html).xpath(
                '//table[@class="table1"]//tr[@name="zbjgTr"]')
            target_trs_len = len(target_trs)

            supplier_name_list = []
            supplier_addr_list = []
            winning_amt_list = []
            order_name_list = []
            order_id_list = []
            # 1 条 target 对应 supplier 2
            # 7 条 target 对应 supplier 2, 4, 6, 8, 10, 12, 14
            for target_trs_index in range(target_trs_len):

                # print(target_trs_index)
                supplier_index = (target_trs_index + 1) * 2
                order_id_list.append(str(target_trs_index + 1))

                order_name = Selector(text=doc_html).xpath(
                    f'//table[@class="Content"]//table[@class="table1"]//tr[{supplier_index}]//td[2]/text()').get() or ''
                supplier_name = Selector(text=doc_html).xpath(
                    f'//table[@class="Content"]//table[@class="table1"]//tr[{supplier_index}]//td[3]/text()').get() or ''

                supplier_addr = Selector(text=doc_html).xpath(
                    f'//table[@class="Content"]//table[@class="table1"]//tr[{supplier_index}]//td[4]/text()').get() or ''

                winning_amt = Selector(text=doc_html).xpath(
                    f'//table[@class="Content"]//table[@class="table1"]//tr[{supplier_index}]//td[5]/text()').get() or ''

                supplier_name_list.append(supplier_name)
                supplier_addr_list.append(supplier_addr)
                order_name_list.append(order_name)
                winning_amt_list.append(winning_amt.replace(",", ''))

            # print('supplier_name_list, supplier_addr_list, winning_amt_list')
            # print(supplier_name_list)
            # print(supplier_addr_list)
            # print(winning_amt_list)

            supplier_name = ",".join(supplier_name_list)
            supplier_addr = ",".join(supplier_addr_list)
            winning_amt = ','.join(winning_amt_list)
            order_name = ','.join(order_name_list)
            order_id = ','.join(order_id_list)

            winning_order_cnt = target_trs_len

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

            new_item = [
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

            # print(new_item)

            self.result_df.loc[len(self.result_df)] = new_item

            # print(self.result_df)
            # return item

    def closed(self, reason):
        print(f'spider henan closed {reason}')
        pass
