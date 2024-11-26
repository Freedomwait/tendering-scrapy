import re


class Re_bj():
    def __init__(self, str):
        self.str = str
        pass

    def total_count(self):
        result = re.findall('找到相关结果约(.*?)条', self.str)
        return result[0] if len(result) else ''

    def project_code(self):
        result = re.findall('项目编号：(.*?)二、项目名称', self.str)
        return result[0] if len(result) else ''

    def project_name(self):
        result = re.findall('项目名称：(.*?)三、中标（成交）信息', self.str)
        return result[0] if len(result) else ''

    def project_winning_amt(self):
        result = re.findall('总中标成交金额：(.*?)中标成交供应商名称', self.str)
        return result[0] if len(result) else ''

    def spplier_name(self):
        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]
        return re.findall('中标成交供应商名称：(.*?)中标成交供应商地址', content)

    def spplier_addr(self):
        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]
        return re.findall('中标成交供应商地址：(.*?)中标金额', content)

    def winning_amt(self):
        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]
        return re.findall('中标金额：(.*?)供应商名称', content)

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

    def agency_contact(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("3.项目联系方式")]

        result = re.findall('联系方式：(.*?)$', content)
        return result[0] if len(result) else ''
