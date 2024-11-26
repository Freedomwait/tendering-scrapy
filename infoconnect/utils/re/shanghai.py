import re


class Re_Shanghai():
    def __init__(self, str):
        self.str = str
        pass

    def project_name(self):
        content = self.str[self.str.find(
            "项目基本情况"):self.str.find("申请人的资格要求")]

        result = re.findall('项目名称：(.*?)预算编号：', content)
        return result[0] if len(result) else ''

    def supplier_name(self):
        content = self.str[self.str.find(
            "成交信息："):self.str.find("主要成交标的")]

        result = re.findall('成交供应商：(.*?)，成交供应商地址', content)
        return result[0] if len(result) else ''

    def supplier_addr(self):
        content = self.str[self.str.find(
            "成交信息："):self.str.find("主要成交标的")]

        result = re.findall('成交供应商地址：(.*?)，成交金额：', content)
        return result[0] if len(result) else ''

    def winning_amt(self):
        content = self.str[self.str.find(
            "成交信息："):self.str.find("主要成交标的")]

        result = re.findall('，成交金额：(.*?)三、', content)
        return result[0] if len(result) else ''

     # 招标代理名称
    def bidding_agent_name(self):
        agent_name = re.findall("采购代理机构信息名称：(.*?)地址：", self.str)
        return agent_name

    # 招标代理名称地址
    def bidding_agent_purchaser_address(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("项目联系方式")]

        result = re.findall('地址：(.*?)联系方式', content)
        return result[0] if len(result) else ''

    # 招标代理名称联系人
    def bidding_agent_purchaser_person(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("同级政府采购监督管理部门名称")]

        result = re.findall('项目联系人（询问）：(.*?)项目联系方式（询问）', content)
        return result[0] if len(result) else ''

    # 招标代理名称联系人对应联系方式
    def bidding_agent_purchaser_contact(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("3.项目联系方式")]

        result = re.findall('联系方式：(.*?)$', content)
        return result[0] if len(result) else ''

     # 采购人名称
    def buyer_name(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("采购代理机构信息")]
        return re.findall('采购人信息名称：(.*?)地址', content)

    # 采购联系人
    def buyer_contact(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("采购代理机构信息")]
        return re.findall('项目联系人：(.*?)联系方式', content)

    # 采购人地址
    def buyer_addr(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("采购代理机构信息")]
        return re.findall('地址：(.*?)联系方式', content)

    # 采购联系人对应联系方式
    def buyer_phone(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("2.采购代理机构信息")]

        return re.findall('联系方式：(.*?)$', content)

    def purchase_dead_line(self):
        # 采购截止时间
        result = re.findall('开标时间：(.*?)开标地点', self.str)

        if len(result) == 0:
            content = self.str[self.str.find(
                "响应文件提交（上传）"):self.str.find("响应文件开启")]
            result = re.findall('截止时间：(.*?)地点', content)

        if len(result) == 0:
            content = self.str[self.str.find(
                "响应文件提交"):self.str.find("开启")]
            result = re.findall('截止时间：(.*?)地点', content)

        if len(result) == 0:
            content = self.str[self.str.find(
                "提交投标文件截止时间、开标时间和地点"):self.str.find("公告期限")]
            result = re.findall('时间：(.*?)提交投标文件', content)

        return result[0] if len(result) else ''

    def budget_account(self):
        content = self.str[self.str.find(
            "项目基本情况"):self.str.find("申请人的资格要求")]

        result = re.findall('预算金额（元）：(.*?)最高限价（元）：', content)
        return result[0] if len(result) else ''

    def max_amt(self):
        content = self.str[self.str.find(
            "项目基本情况"):self.str.find("申请人的资格要求")]

        result = re.findall('最高限价（元）：(.*?)采购需求', content)
        return result[0] if len(result) else ''

    def order_packages(self):
        content = self.str[self.str.find(
            "项目基本情况"):self.str.find("申请人的资格要求")]

        return re.findall('包名称：(.*?)数量', content)
