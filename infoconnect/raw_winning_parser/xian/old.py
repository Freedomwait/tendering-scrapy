import re
from scrapy.selector import Selector
from infoconnect.utils.nodeparse import NodeParse


class Raw_Result_Parser_Old():
    model = {
        'project_id': "",
        'winning_date': "",
        'winning_notice_url': "",
        'supplier_name': "",
        'supplier_addr': "",
        "order_name": "",
        "winning_amt": "",
        "cadidate_name": "",
        "buyer_name": "",
        "buyer_addr": "",
        "buyer_contact": "",
        "agency_name": "",
        "agency_addr": "",
        "agency_contact": "",
    }

    def __init__(self, response, main_content_xpath):
        self.response = response
        self.doc_html = response.body.decode('utf-8')
        main_content = Selector(text=self.doc_html).xpath(main_content_xpath)
        text = NodeParse(main_content).to_text()
        self.text = text

    def project_id(self):
        result = re.findall('项目编号：(.*?)二、项目名称', self.text)
        return result[0] if len(result) else ''

    def winning_date(self):
        return Selector(text=self.doc_html).xpath('//span[@id="noticeTime"]//i/text()').get()

    def winning_notice_url(self):
        return self.response.url

    def supplier_name(self):
        content = self.text[self.text.find(
            "三、中标信息"):self.text.find("四、主要标的信息")]

        if (len(content) == 0):
            content = self.text[self.text.find(
                "三、采购结果"):self.text.find("四、主要标的信息")]

        result = re.findall('供应商名称：(.*?)供应商地址', content)
        return result[0] if len(result) else ''

    def supplier_addr(self):
        content = self.text[self.text.find(
            "三、中标信息"):self.text.find("四、主要标的信息")]
        if (len(content) == 0):
            content = self.text[self.text.find(
                "三、采购结果"):self.text.find("四、主要标的信息")]

        result = re.findall('供应商地址：(.*?)中标金额：', content)
        return result[0] if len(result) else ''

    def order_name(self):
        result = re.findall('项目名称：(.*?)三、中标信息', self.text)
        if (len(result) == 0):
            result = re.findall('项目名称：(.*?)三、采购结果', self.text)
        return result[0] if len(result) else ''

    def winning_amt(self):
        content = self.text[self.text.find(
            "三、中标信息"):self.text.find("四、主要标的信息")]
        if (len(content) == 0):
            content = self.text[self.text.find(
                "三、采购结果"):self.text.find("四、主要标的信息")]

        result = re.findall('中标金额：(.*?)$', content)
        result_list = []
        for item in result:
            result_list.append(str(item).replace(',', ''))
        return result_list

    def cadidate_name(self):
        return None

    def buyer_name(self):
        content = self.text[self.text.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.text.find("项目联系方式")]

        result = re.findall('采购人信息名称：(.*?)地址', content)
        return result[0] if len(result) else ''

    def buyer_addr(self):
        content = self.text[self.text.find(
            "采购人信息"):self.text.find("采购代理机构信息")]

        result = re.findall('地址：(.*?)联系方式', content)
        return result[0] if len(result) else ''

    def buyer_contact(self):
        content1 = self.text[self.text.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.text.find("项目联系方式")]
        content = content1[content1.find(
            "采购人信息"):content1.find("2.采购代理机构信息")]

        result = re.findall('联系方式：(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方式:(.*?)$', content)
        return result[0] if len(result) else ''

    def agency_name(self):
        content1 = self.text[self.text.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.text.find("项目联系方式")]
        content = content1[content1.find(
            "采购代理机构信息"):content1.find("项目联系方式")]

        result = re.findall('名称：(.*?)地址', content)
        if len(result) == 0:
            result = re.findall('名称:(.*?)地址', content)
        return result[0] if len(result) else ''

    def agency_addr(self):
        content1 = self.text[self.text.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.text.find("项目联系方式")]
        content = content1[content1.find(
            "采购代理机构信息"):content1.find("项目联系方式")]

        result = re.findall('地址：(.*?)联系方式', content)
        if len(result) == 0:
            result = re.findall('地址：(.*?)联系方法', content)
        if len(result) == 0:
            result = re.findall('地址:(.*?)联系方式', content)
        if len(result) == 0:
            result = re.findall('地址:(.*?)方法', content)
        return result[0] if len(result) else ''

    def agency_contact(self):
        content1 = self.text[self.text.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.text.find("项目联系方式")]
        content = content1[content1.find(
            "采购代理机构信息"):content1.find("项目联系方式")]

        result = re.findall('联系方式：(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方式:(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方法:(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方法：(.*?)$', content)
        return result[0] if len(result) else ''

    def export_dict(self):
        self.model["project_id"] = self.project_id()
        self.model["winning_date"] = self.winning_date()
        self.model["winning_notice_url"] = self.winning_notice_url()
        self.model["supplier_name"] = self.supplier_name()
        self.model["supplier_addr"] = self.supplier_addr()
        self.model["order_name"] = self.order_name()
        self.model["winning_amt"] = self.winning_amt()
        self.model["cadidate_name"] = self.cadidate_name()
        self.model["buyer_name"] = self.buyer_name()
        self.model["buyer_addr"] = self.buyer_addr()
        self.model["buyer_contact"] = self.buyer_contact()
        self.model["agency_name"] = self.agency_name()
        self.model["agency_addr"] = self.agency_addr()
        self.model["agency_contact"] = self.agency_contact()

        return self.model
