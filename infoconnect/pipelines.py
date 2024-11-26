# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from infoconnect.conf.index import TASK


class MysqlPipeline:

    def process_item(self, item, spider):

        CODE = TASK["TASK_CODE"]
        agent_name = ','.join(item["招标代理名称"]) if len(item["招标代理名称"]) else ''
        bid_amount = ','.join(item["中标金额"]) if len(item["中标金额"]) else ''
        winning_bidder = ''.join(item["中标单位"]) if len(item["中标单位"]) else ''
        exentd_file = ''.join(item["附件"]) if len(item["附件"]) else ''
        spider.cur.execute(""" 
        insert into notice_result{CODE} (
            keyword,
            area,
            customer_type,
            purchaser_name,
            purchaser_person,
            purchaser_contact,
            bidding_time,
            winning_bidding_time,
            bidding_agent_name,
            project_name,
            product,
            specifications,
            price,
            url,
            bid_amount,
            winning_bidder,
            appendix,
            content
            ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item["查询关键词"],
            item["地区"],
            item["客户类型"],
            item["采购人名称"],
            item["采购项目联系人"],
            item["采购项目联系人联系方式"],
            item["招标时间"],
            item["中标时间"],
            agent_name,
            item["项目名称"],
            item["产品"],
            item["参数"],
            item["单价"],
            item["网站链接"],
            bid_amount,
            winning_bidder,
            exentd_file,
            item["Text"]
        ))

        spider.conn.commit()
        return item


class MysqlDetailPipeline:
    def process_item(self, item, spider):
        spider.cur.execute(""" 
        insert into test (
            keyword,
            url
            ) values (%s,%s)""", (
            item["项目名称"],
            item["网站链接"]
        ))

        # Execute insert of data into database
        spider.conn.commit()
        return item
