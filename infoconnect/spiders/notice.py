import datetime
import math
import json
import re
# import mysql.connector
import scrapy
from scrapy.selector import Selector
from urllib.parse import urlparse, parse_qs
from infoconnect.utils.index import Utils
from infoconnect.utils.nodeparse import NodeParse, node_text
from infoconnect.utils.queryfactory import QueryFactory
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.school import School
from infoconnect.conf.index import KEYWORD_DIC, TASK


class NoticeSpider(scrapy.Spider):
    name = 'notice'
    allowed_domains = ['zfcgmanager.czt.zj.gov.cn']

    list_base_url = "https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results"

    detail_base_url = "https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html"

    start_urls = [
        'https://zfcg.czt.zj.gov.cn/'
    ]

    custom_settings = {
        "FEEDS": {
            f'out/notice_{TASK["TASK_CODE"]}.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/notice_{TASK["TASK_CODE"]}.log',
        "LOG_FILE_APPEND": False
    }

    def __init__(self):
        super().__init__()

        self.logger.info("=====  start task  ======")
        self.logger.info(TASK)

        # 创建公告和采购关联文件
        self.rfile = open(
            f'sql/related_purchase_announcement{TASK["TASK_CODE"]}.txt', 'w')

        # 创建公告和合同关联文件
        self.rcfile = open(
            f'sql/related_contract_announcement{TASK["TASK_CODE"]}.txt', 'w')
        pass

    def parse(self, response):
        # TODO 暂时未抓取到
        # body_utm = response.css('body::attr(data-utm-b)').get()

        # 调整需要关键词组
        keyword_list = TASK["keyword_list"]

        # 根据查询条件构造列表查询请求
        for keyword in keyword_list:
            query = QueryFactory().keyword(keyword).time(
                TASK["time_range_type"]).isExact(TASK["isExact"]).build()

            list_url = UrlFactory(self.list_base_url, query).build()

            yield scrapy.Request(list_url, meta={"keyword": keyword}, callback=self.parse_list)

    # 处理列表页分页
    def parse_list(self, response):
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        self.logger.debug('list responseStr')
        self.logger.debug(responseStr)
        keyword = response.meta["keyword"]

        # 第一次只拿分页信息抓全量的列表数据，之后再处理
        if responseJson["successFlag"] == True:
            # pagenation
            pageSize = 100
            totalCount = responseJson["realCount"] or responseJson["count"]
            totalPage = math.ceil(totalCount / pageSize)
            self.logger.info(
                f'pagenation info: realCount:{responseJson["realCount"]}, count: {responseJson["count"]}, totalPage: {totalPage} ')
            for current_page in range(totalPage):
                detail_query = QueryFactory().keyword(keyword).time(TASK["time_range_type"]).isExact(TASK["isExact"]).pageNo(
                    current_page + 1).build()
                detail_url = UrlFactory(
                    self.list_base_url, detail_query).build()

                yield scrapy.Request(detail_url, meta={"keyword": keyword}, callback=self.parse_item)

    # 处理列表数据
    def parse_item(self, response):
        responseStr = str(response.body, encoding="utf-8")
        responseJson = json.loads(responseStr)
        keyword = response.meta["keyword"]

        if responseJson["successFlag"] == True:
            # 分页信息已处理，这里只解析参数
            articles = responseJson["articles"]
            for article in articles:
                article_url = article['url']
                # 地区
                districtName = article['districtName']

                # 关键词
                # keywords = article['keywords']

                # 项目名称
                projectName = article['projectName']
                projectCode = article['projectCode']

                notice_id = parse_qs(urlparse(article_url).query)[
                    'noticeId'][0]
                detail_url = UrlFactory('https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results', {
                    "noticeId": notice_id,
                    "url": "noticeDetail"
                }).build()
                yield scrapy.Request(detail_url, meta={
                    "keyword": keyword,
                    "districtName": districtName,
                    "projectName": projectName,
                    "noticeId": notice_id,
                    "projectCode": projectCode,
                    # "keywords": keywords
                }, callback=self.parse_detail)

    # 处理详情页数据
    def parse_detail(self, response):
        url = response.url

        resJson = json.loads(response.body)

        # 标的名称 品牌 规格型号 单价
        target_name = ''
        brand_name = ''
        specifications = ''
        price = ''
        bid_amount = ''
        winning_bidder = ''

        # 过滤废标公告
        notice_title = resJson["noticeTitle"]
        notice_ls = re.findall('废标公告$', notice_title)
        if len(notice_ls):
            self.logger.info(f'废标过滤掉{url}')
            pass
        else:
            table_list = Selector(
                text=resJson['noticeContent']).xpath('//table')

            # 表格解析
            for table in table_list:
                rows_header = table.xpath('.//tr//th//text()').getall() or []
                rows_body = table.xpath('.//tr//td//text()').getall() or []

                table_text = node_text(table)

                if (table_text.find('中标供应商名称') != -1):
                    # TODO
                    # self.logger.info('中标表格信息')
                    def parse_table_with_header(rows_header, rows_body, value):
                        n_index = -1
                        for index in range(len(rows_body)):
                            if (value in rows_header[index]):
                                n_index = index
                                break
                        if n_index != -1 and n_index < len(rows_body):
                            return rows_body[n_index]

                        return ''

                    if len(rows_header):
                        bid_amount = parse_table_with_header(
                            rows_header, rows_body, "中标（成交）金额")
                        winning_bidder = parse_table_with_header(
                            rows_header, rows_body, "中标供应商名称")
                    else:
                        col_number = 4
                        bid_amount = self.parse_table(
                            rows_body, col_number, "中标（成交）金额")
                        winning_bidder = self.parse_table(
                            rows_body, col_number, "中标供应商名称")
                    pass

                if (table_text.find('标的名称') != -1):
                    # 标的信息里的数据没有 th，都在 td 里面，所以多一步解析步骤
                    # 目前只有 7 列，所以后面的部分拆分出来
                    col_number = 7
                    target_name = self.parse_table(
                        rows_body, col_number, "标的名称")
                    brand_name = self.parse_table(rows_body, col_number, "品牌")
                    specifications = self.parse_table(
                        rows_body, col_number, "规格型号")
                    price = self.parse_table(rows_body, col_number, "单价(元)")

                if (table_text.find('专家') != -1):
                    # TODO
                    # self.logger.info('技术评分明细表')
                    pass

            selector = Selector(text=resJson['noticeContent']).xpath('//body')
            text = NodeParse(selector).to_text()
            util = Utils(text, url)

            bidding_time = ''
            winning_bidding_time = ''
            relevantArticles = resJson['relevantArticles'] or []
            if (len(relevantArticles)):

                # 合同公告是一个列表
                contract_report_list = []

                for item in relevantArticles:
                    # 招标类型2，中标类型5，合同公告 6
                    if item["type"] == 2 and item["pubDate"]:
                        pub_date = datetime.datetime.strptime(
                            item["pubDate"], '%Y-%m-%d %H:%M:%S')
                        bidding_time = pub_date.strftime("%Y-%m-%d")
                        self.rfile.write(
                            f"""{response.meta["noticeId"]},{item["id"]},{item["projectCode"]}\n""")

                    if item["type"] == 5 and item["pubDate"]:
                        pub_date = datetime.datetime.strptime(
                            item["pubDate"], '%Y-%m-%d %H:%M:%S')
                        winning_bidding_time = pub_date.strftime("%Y-%m-%d")

                    # 合同公告
                    if item["type"] == 6 and item["id"]:
                        contract_report_list.append(item["id"])

                # 写入关联文件
                self.rcfile.write(
                    f"""{response.meta["noticeId"]},{contract_report_list},{item["projectCode"]}\n""")

            item = {}
            item["exact_matched"] = self.exactMatch(
                response.meta["keyword"], text)
            item["查询关键词"] = response.meta["keyword"]
            # item["keywords"] = response.meta["keywords"]
            item["地区"] = response.meta["districtName"]
            purchaser_name = util.purchaser_name()
            item["客户类型"] = School(purchaser_name).get_customer_type()
            item["采购人名称"] = purchaser_name
            item["采购项目联系人"] = util.purchaser_person()
            item["采购项目联系人联系方式"] = util.purchaser_contact()
            item["招标时间"] = bidding_time
            item["中标时间"] = winning_bidding_time
            item["招标代理名称"] = util.bidding_agent_name()
            item["采购代理机构_项目联系人"] = util.bidding_agent_purchaser_person()
            item["采购代理机构_项目联系方式"] = util.bidding_agent_purchaser_contact()

            item["项目名称"] = response.meta["projectName"]
            item["项目编号"] = response.meta["projectCode"]
            # text 解析无法结构化，用原始的 table 进行解析
            item["产品"] = target_name
            item["品牌"] = brand_name
            item["参数"] = specifications
            item["单价"] = price

            item["网站链接"] = UrlFactory(
                self.detail_base_url, {"noticeId": response.meta["noticeId"]}).build()
            # item["最高限价"] = util.maximum_price()
            item["中标金额"] = bid_amount
            item["中标单位"] = winning_bidder

            link_list = []
            all_link = Selector(text=resJson['noticeContent']).css(
                'ul.fjxx>li>p>a::attr(href)').getall()
            # all_link_text = Selector(text=resJson['noticeContent']).xpath('//a//text()').getall()
            for index in range(len(all_link)):
                # TODO 多组超链接
                # link_list.append(f'=HYPERLINK("{all_link[index]}","{all_link_text[index]}")')
                link_list.append(all_link[index])
                pass
            item["附件"] = '\n'.join(link_list)
            # item["Text"] = text

            yield item

    # 按照字典匹配
    def exactMatch(self, keyword, text):
        str = "N"
        for key, value in KEYWORD_DIC.items():
            result = []
            result.append(key)
            for item in value:
                result.append(item)

            if keyword == key:
                for res in result:
                    if (text.find(res) != -1):
                        str = "Y"
                        break
        return str

    # 解析表格对应关系，主要针对多个标的
    def parse_table(self, rows_body, col_number, key):
        col = col_number
        _result = []
        try:
            n_index = -1
            for index in range(len(rows_body)):
                if (key in rows_body[index]):
                    n_index = index
                    break
            # 多个标的情况
            items = int(len(rows_body) / col)
            if items > 2:
                for item in range(items):
                    if item > 0 and n_index != -1 and n_index + col * item + 1 < len(rows_body):
                        _result.append(rows_body[n_index + col * item])
            else:
                # 老的模板里可能匹配不到
                if n_index + col < len(rows_body):
                    _result = rows_body[n_index + col]

        except ValueError:
            self.logger.info(f"无标{key}")

        return _result

    def closed(self, reason):
        self.rfile.close()
        self.rcfile.close()
        self.logger.info(f'spider detail closed {reason}')
        pass
