import scrapy


class SplashSpider(scrapy.Spider):
    name = "splash"
    allowed_domains = ["www.ccgp-anhui.gov.cn"]
    start_urls = [
        "http://localhost:8050/render.html?url=http://www.ccgp-hebei.gov.cn/cz/cz_ys/cggg/zhbggAAAA/202207/t20220720_1637968.html"]

    def parse(self, response):
        self.logger.info(u'---------我这个是简单的测试页面---------')

        print(response.body)
        small_title = response.xpath(
            '////table[@id="ServiceSupplierInfo"]').getall()
        self.logger.info(u"find：%s" % small_title)
        self.logger.info(u'---------------success----------------')
