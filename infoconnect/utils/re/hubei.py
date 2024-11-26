import re


class Re_Hubei():
    def __init__(self, str):
        self.str = str
        pass

    def total_count(self):
        result = re.findall('为您找到了约“(.*?)”条结果', self.str)
        return result[0] if len(result) else ''

    def pub_date(self):
        result = re.findall('发布日期：(.*?)｜发布单位：', self.str)
        return result[0] if len(result) else ''

    def project_code(self):
        result = re.findall('项目编号(.*?)二、采购计划', self.str)
        return result[0] if len(result) else ''

    def order_name(self):
        result = re.findall('三、项目名称(.*?)四、中标（成交）信息', self.str)
        return result[0] if len(result) else ''

    def supplier_name(self):
        result = re.findall('供应商名称：(.*?)供应商地址：', self.str)
        return result[0] if len(result) else ''

    def supplier_addr(self):
        result = re.findall('供应商地址：(.*?)中标（成交）金额', self.str)
        return result[0] if len(result) else ''

    def winning_amt(self):
        result = re.findall('中标（成交）金额：(.*?)工程类', self.str)
        # result1 = re.findall('中标（成交）金额：(.*?)货物类', self.str)

        if len(result) == 0:
            result = re.findall('中标（成交）金额：(.*?)货物类', self.str)
            if len(result) == 0:
                result = re.findall('中标（成交）金额：(.*?)服务类', self.str)

        return result[0] if len(result) else ''

    def buyer_name(self):
        content = self.str[self.str.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]

        result = re.findall('采购人信息名称：(.*?)地址', content)
        return result[0] if len(result) else ''

    def buyer_addr(self):
        content = self.str[self.str.find(
            "采购人信息"):self.str.find("采购代理机构信息")]

        result = re.findall('地址：(.*?)联系方式', content)
        return result[0] if len(result) else ''

    def buyer_contact(self):
        content1 = self.str[self.str.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
        content = content1[content1.find(
            "采购人信息"):content1.find("2、采购代理机构信息")]

        result = re.findall('联系方式：(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方式:(.*?)$', content)
        return result[0] if len(result) else ''

    def agent_name(self):
        content1 = self.str[self.str.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
        content = content1[content1.find(
            "采购代理机构信息"):content1.find("项目联系方式")]

        result = re.findall('名称：(.*?)地址', content)
        if len(result) == 0:
            result = re.findall('名称:(.*?)地址', content)
        return result[0] if len(result) else ''

    def agent_addr(self):
        content1 = self.str[self.str.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
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

    def agent_contact(self):
        content1 = self.str[self.str.find(
            "凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
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
