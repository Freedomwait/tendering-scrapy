import re


class Re_Ccgp():
    def __init__(self, str):
        self.str = str
        pass

    def project_id(self):
        result = re.findall('项目编号：(.*?)（招标文件编号', self.str)
        return result[0] if len(result) else ''

    def project_name(self):
        result = re.findall('项目名称：(.*?)三、中标', self.str)
        return result[0] if len(result) else ''

    def supplier_name(self):
        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]

        return re.findall('供应商名称：(.*?)供应商地址：', content)

    def supplier_addr(self):
        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]

        return re.findall('供应商地址：(.*?)中标（成交）金额', content)

    def winning_amt(self):

        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("四、主要标的信息")]

        return re.findall('中标（成交）金额：(.*?)$', content)

    def winning_amt_zy(self):

        content = self.str[self.str.find(
            "三、中标（成交）信息"):self.str.find("主要标的信息")]

        # print(f"len(self.supplier_name()): {len(self.supplier_name())}")

        if len(self.supplier_name()) == 1:
            return re.findall('中标（成交）金额：(.*?)四、', content)
        elif len(self.supplier_name()) > 1:
            other = re.findall('中标（成交）金额：(.*?)四、', content)
            # print(f'other: {other}')
            if (len(other)):
                othet_content = other[0]
                first_amt = re.findall('^(.*?)供应商名称', othet_content) or []
                # print(f'first_amt: {first_amt}')

                middle_amt = re.findall(
                    '（成交）金额：(.*?)供应商名称', othet_content) or []

                last_content = othet_content[othet_content.find(
                    middle_amt[len(middle_amt) - 1]):]

                last_amt = re.findall('金额：(.*?)$', last_content) or []

                # print(
                # f"first_amt, middle_amt, last_amt: {first_amt}, {middle_amt}, {last_amt}")

                return first_amt + middle_amt + last_amt

        pass

    def publish_date(self):
        result = re.findall('5、评审日期：(.*?)二、采购项目用途', self.str)
        return result[0] if len(result) else ''

    def order_name(self):
        result = re.findall('二、项目名称：(.*?)三、中标（成交）信息', self.str)
        return result[0] if len(result) else ''

    def buyer_name(self):
        content = self.str[self.str.find(
            "九、凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]

        result = re.findall('采购人信息名称：(.*?)地址', content)
        return result[0] if len(result) else ''

    def buyer_addr(self):
        content1 = self.str[self.str.find(
            "九、凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
        content = content1[content1.find(
            "1.采购人信息"):content1.find("2.采购代理机构信息")]

        result = re.findall('地址：(.*?)联系方式', content)
        if len(result) == 0:
            result = re.findall('地址:(.*?)联系方式', content)
        return result[0] if len(result) else ''

    def buyer_contact(self):
        content1 = self.str[self.str.find(
            "九、凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
        content = content1[content1.find(
            "1.采购人信息"):content1.find("2.采购代理机构信息")]

        result = re.findall('联系方式：(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方式:(.*?)$', content)
        return result[0] if len(result) else ''

    def agent_name(self):
        content1 = self.str[self.str.find(
            "九、凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
        content = content1[content1.find(
            "采购代理机构信息"):content1.find("项目联系方式")]

        result = re.findall('名称：(.*?)地址', content)
        if len(result) == 0:
            result = re.findall('名称:(.*?)地址', content)
        return result[0] if len(result) else ''

    def agent_addr(self):
        content1 = self.str[self.str.find(
            "九、凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
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
            "九、凡对本次公告内容提出询问，请按以下方式联系"):self.str.find("项目联系方式")]
        content = content1[content1.find(
            "采购代理机构信息"):content1.find("3.项目联系方式")]

        result = re.findall('联系方式：(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方式:(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方法:(.*?)$', content)
        if len(result) == 0:
            result = re.findall('联系方法：(.*?)$', content)
        return result[0] if len(result) else ''
