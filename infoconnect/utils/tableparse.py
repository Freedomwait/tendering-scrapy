class TableParse:
    def __init__(self, selector):
        self.selector = selector
        print(self.selector)
        print(self.selector.get())
    
    # 结构化数据
    def data(self):
        # rows = self.selector.xpath('//thead//tr')

        rows_header = self.selector.xpath('.//thead//tr//th//text()').getall()
        rows_body = self.selector.xpath('.//tbody//tr//td//text()').getall()

        # 第一行是表头，后面的是数据

        return {
            "rows_header": rows_header,
            "rows_body": rows_body
        }

    # 提取结构化数据    
    def get_data(self, th_text):
        data = self.data()

        print('data')
        print(data)
        rows_header = data["rows_header"]
        rows_body = data["rows_body"]

        index = rows_header.index(th_text)
        if index is not -1:
            return rows_body[index]
        else:
            return ''