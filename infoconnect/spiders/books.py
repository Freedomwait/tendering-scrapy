import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(
            allow='.html',
            restrict_xpaths="/html[@class='no-js']/body[@id='default']/div[@class='container-fluid page']/div[@class='page_inner']/div[@class='row']/div[@class='col-sm-8 col-md-9']"),
            callback='parse',
            follow=True),
    )

    def parse(self, response):
        item = {}

        item['book_name'] = response.xpath("/html[@class='no-js']/body[@id='default']/div[@class='container-fluid page']/div[@class='page_inner']/div[@class='content']/div[@id='content_inner']/article[@class='product_page']/div[@class='row']/div[@class='col-sm-6 product_main']/h1/text()").get()
        yield item
