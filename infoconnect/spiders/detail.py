
import scrapy
from scrapy.selector import Selector
import re
import json
import datetime
# import mysql.connector
# from infoconnect.conf.db import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
from infoconnect.utils.school import School
from infoconnect.utils.index import Utils
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.nodeparse import NodeParse, node_text


class NoticeSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['zfcgmanager.czt.zj.gov.cn']

    custom_settings = {
        "FEEDS": {
            'out/detail.csv': {'format': 'csv', 'overwrite': True}
        },
        "LOG_FILE": f'log/detail.log',
        "LOG_FILE_APPEND": False
    }

    detail_url_base = 'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results'

    detail_base_url = "https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html"

    notice_id = 8991124

    start_url = UrlFactory(
        detail_url_base, {"noticeId": notice_id, "url": "noticeDetail"}).build()

    start_urls = [
        start_url
    ]

    def __init__(self):
        super().__init__()
        # self.conn = mysql.connector.connect(
        #     host=DB_HOST,
        #     user=DB_USER,
        #     port=DB_PORT,
        #     password=DB_PASSWORD,
        #     database=DB_DATABASE,
        # )
        # self.cur = self.conn.cursor()
        pass

    def parse(self, response):
        url = response.url

        resJson = json.loads(response.body)
        # print('resJson', resJson)

        # 标的名称 品牌 规格型号 单价 中标金额，中标单位
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
            print(f'废标过滤掉{url}')
            pass
        else:
            table_list = Selector(
                text=resJson['noticeContent']).xpath('//table')

            # 表格解析
            for table in table_list:
                rows_header = table.xpath('.//tr//th//text()').getall() or []
                rows_body = table.xpath('.//tr//td//text()').getall() or []

                self.logger.info(f'rows_header {rows_header}')
                self.logger.info(f'rows_body {rows_body}')

                table_text = node_text(table)

                if (table_text.find('中标供应商名称') != -1):
                    # TODO
                    self.logger.info('中标表格信息')

                    def parse_table_with_header(rows_header, rows_body, value):
                        n_index = -1
                        for index in range(len(rows_body)):
                            if (value in rows_header[index]):
                                n_index = index
                                break
                        self.logger.info(f'parse_table_with_header {n_index}')
                        if n_index != -1 and n_index < len(rows_body):
                            return rows_body[n_index]

                        return ''

                    if len(rows_header):
                        self.logger.info('has rows_header')
                        bid_amount = parse_table_with_header(
                            rows_header, rows_body, "中标（成交）金额")
                        winning_bidder = parse_table_with_header(
                            rows_header, rows_body, "中标供应商名称")
                    else:
                        self.logger.info('has no rows_header')

                        col_number = 4
                        bid_amount = self.parse_table(
                            rows_body, col_number, "中标（成交）金额")
                        winning_bidder = self.parse_table(
                            rows_body, col_number, "中标供应商名称")
                    pass

                    # col_number = 4
                    # bid_amount = target_name = self.parse_table(rows_body, col_number, "中标（成交）金额")
                    # winning_bidder = target_name = self.parse_table(rows_body, col_number, "中标供应商名称")
                    # pass

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

                    # try:
                    #     n_index = rows_body.index("标的名称")
                    #     target_name = rows_body[n_index + 7]
                    # except ValueError:
                    #     self.logger.info("无标的名称")
                    #     pass
                    # try:
                    #     n_index = rows_body.index("品牌")
                    #     brand_name = rows_body[n_index + 7]
                    # except ValueError:
                    #     self.logger.info("无品牌")
                    #     pass
                    # try:
                    #     p_index = rows_body.index("规格型号")
                    #     specifications = rows_body[p_index + 7]
                    # except ValueError:
                    #     self.logger.info("无规格型号")
                    #     pass
                    # try:
                    #     price_index = rows_body.index("单价(元)")
                    #     price = rows_body[price_index + 7]
                    # except ValueError:
                    #     self.logger.info("无单价")
                    #     pass

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
                for item in relevantArticles:
                    # 招标类型2，中标类型5
                    if item["type"] == 2 and item["pubDate"]:
                        pub_date = datetime.datetime.strptime(
                            item["pubDate"], '%Y-%m-%d %H:%M:%S')
                        bidding_time = pub_date.strftime("%Y-%m-%d")
                    if item["type"] == 5 and item["pubDate"]:
                        pub_date = datetime.datetime.strptime(
                            item["pubDate"], '%Y-%m-%d %H:%M:%S')
                        winning_bidding_time = pub_date.strftime("%Y-%m-%d")

            item = {}
            item["地区"] = "Done"
            item["采购人名称"] = util.purchaser_name()
            item["客户类型"] = School(util.purchaser_name()).get_customer_type()
            item["采购项目联系人"] = util.purchaser_person()
            item["采购项目联系人联系方式"] = util.purchaser_contact()

            item["招标时间"] = bidding_time
            item["中标时间"] = winning_bidding_time

            item["招标代理名称"] = util.bidding_agent_name()
            item["采购代理机构_项目联系人"] = util.bidding_agent_purchaser_person()
            item["采购代理机构_项目联系方式"] = util.bidding_agent_purchaser_contact()

            item["项目名称"] = "Done"

            # text 解析无法结构化，用原始的 table 进行解析
            item["产品"] = target_name
            item["参数"] = specifications
            item["单价"] = price
            item["品牌"] = brand_name

            item["网站链接"] = UrlFactory(
                self.detail_base_url, {"noticeId": self.notice_id}).build()

            item["最高限价"] = util.maximum_price()
            item["采购截止时间"] = util.purchase_dead_line()
            item["中标金额"] = bid_amount
            item["中标单位"] = winning_bidder

            item["mainSubjectInfo"] = util.mainSubjectInfo()

            link_list = []
            # 只保留最后的附件
            all_link = Selector(text=resJson['noticeContent']).css(
                'ul.fjxx>li>p>a::attr(href)').getall()
            # all_link_text = Selector(text=resJson['noticeContent']).xpath('//a//text()').getall()
            for index in range(len(all_link)):
                # TODO 多组超链接
                # link_list.append(f'=HYPERLINK("{all_link[index]}","{all_link_text[index]}")')
                link_list.append(all_link[index])
                pass
            item["附件"] = '\n'.join(link_list)
            item["Text"] = text

            yield item

    def parse_table(self, rows_body, col_number, key):
        col = col_number
        _result = []
        try:
            n_index = -1
            self.logger.info(f"len(rows_body) {len(rows_body)}")
            for index in range(len(rows_body)):
                self.logger.info(f"key in {index} {len(rows_body)}")
                if (key in rows_body[index]):
                    n_index = index
                    break
            # n_index = rows_body.index(key)
            # 多个标的情况
            items = int(len(rows_body) / col)
            if items > 2:
                for item in range(items):
                    if item > 0 and n_index != -1 and n_index + col * item + 1 < len(rows_body):
                        self.logger.info('n_index + col * item')
                        self.logger.info(f'{len(rows_body)}')
                        self.logger.info(n_index + col * item)
                        _result.append(rows_body[n_index + col * item])
            else:
                if n_index + col < len(rows_body):
                    _result = rows_body[n_index + col]

        except ValueError:
            self.logger.info(f"无{key}")

        return _result

    def closed(self, reason):
        # self.conn.close()
        # self.cur.close()
        print(f'spider detail closed {reason}')
        pass
