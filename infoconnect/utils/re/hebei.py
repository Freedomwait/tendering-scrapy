import re


class Re_hebei():
    def __init__(self, str):
        self.str = str
        pass

    def project_id(self):
        result = re.findall('一、项目编号：(.*?)二、项目名称', self.str)
        return result[0] if len(result) else ''

    def publish_date(self):
        result = re.findall('发布时间：(.*?)一、项目编号', self.str)
        return result[0] if len(result) else ''

    def order_name(self):
        result = re.findall('二、项目名称：(.*?)三、中标（成交）信息', self.str)
        return result[0] if len(result) else ''

    def buyer_name(self):
        content = self.str[self.str.find(
            "1.采购人信息"):self.str.find("采购代理机构信息")]

        result = re.findall('名称：(.*?)地址', content)
        return result[0] if len(result) else ''

    def buyer_addr(self):
        content = self.str[self.str.find(
            "1.采购人信息"):self.str.find("采购代理机构信息")]

        result = re.findall('地址：(.*?)联系方式', content)
        return result[0] if len(result) else ''

    def buyer_contact(self):
        content = self.str[self.str.find(
            "1.采购人信息"):self.str.find("2.采购代理机构信息")]

        result = re.findall('联系方式：(.*?)$', content)
        return result[0] if len(result) else ''

    def agent_name(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("项目联系方式")]

        result = re.findall('名称：(.*?)地址', content)
        return result[0] if len(result) else ''

    def agent_addr(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("项目联系方式")]

        result = re.findall('地址：(.*?)联系方式', content)
        return result[0] if len(result) else ''

    def agent_contact(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("3.项目联系方式")]

        result = re.findall('联系方式：(.*?)$', content)
        return result[0] if len(result) else ''
