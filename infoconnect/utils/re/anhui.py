import re


class Re_anhui():
    def __init__(self, str):
        self.str = str
        pass

    def total_count(self):
        result = re.findall('找到相关结果约(.*?)条', self.str)
        return result[0] if len(result) else ''

    def project_code(self):
        result = re.findall('二、项目编号: (.*?)三、采购方式', self.str)
        return result[0] if len(result) else ''

    def project_name(self):
        result = re.findall('一、项目名称: (.*?)二、项目编号: ', self.str)
        return result[0] if len(result) else ''

    def project_winning_amt(self):
        result = re.findall('总中标成交金额：(.*?)中标成交供应商名称', self.str)
        return result[0] if len(result) else ''

    def spplier_name(self):
        content = self.str[self.str.find(
            "七、评审结果："):self.str.find("八、公告期限：公告")]
        result = re.findall('中标单位：(.*?)中标金额：', content)
        return result if len(result) else ''

    def spplier_addr(self):
        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]
        result = re.findall('中标成交供应商地址：(.*?)中标金额', content)
        return result[0] if len(result) else ''

    def winning_amt(self):
        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]
        result = re.findall('中标金额：(.*?)供应商名称', content)
        return result[0] if len(result) else ''
