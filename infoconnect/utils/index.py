import re

digit = {'一': 1, '二': 2, '三': 3, '四': 4,
         '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}


def _trans(s):
    num = 0
    if s:
        idx_q, idx_b, idx_s = s.find('千'), s.find('百'), s.find('十')
        if idx_q != -1:
            num += digit[s[idx_q - 1:idx_q]] * 1000
        if idx_b != -1:
            num += digit[s[idx_b - 1:idx_b]] * 100
        if idx_s != -1:
            # 十前忽略一的处理
            num += digit.get(s[idx_s - 1:idx_s], 1) * 10
        if s[-1] in digit:
            num += digit[s[-1]]
    return num


def parse_table_with_header(rows_header, rows_body, value):
    n_index = -1
    for index in range(len(rows_body)):
        if (value in rows_header[index]):
            n_index = index
            break
    if n_index != -1 and n_index < len(rows_body):
        return rows_body[n_index]

    return ''


def parse_table(rows_body, col_number, key):
    col = col_number
    _result = []
    try:
        n_index = -1
        for index in range(len(rows_body)):
            if (key in rows_body[index]):
                n_index = index
                break
        # 多个标的情况
        items = int(len(rows_body) / col)
        if items > 2:
            for item in range(items):
                if item > 0 and n_index != -1 and n_index + col * item + 1 < len(rows_body):
                    _result.append(rows_body[n_index + col * item])
        else:
            # 老的模板里可能匹配不到
            if n_index + col < len(rows_body):
                _result = rows_body[n_index + col]

    except ValueError:
        print(f"无标{key}")
        _result = []

    return _result


def purchase_type(title):
    purchase_type_list = [
        "公开招标",
        "邀请招标",
        "竞争性谈判",
        "询价",
        "单一来源",
        "竞争性磋商",
        "在线询价",
        "其他",
    ]
    for item in purchase_type_list:
        if item in title:
            return item
        else:
            '其他'
    pass


class Utils:
    def __init__(self, str, url):
        self.str = str
        self.url = url
        pass
    pass

    # # 地区
    # def area(self, area_code):
    #     return area_code or None

    # 客户类型
    def customer_type(self):
        return None

    # 学校名称
    def school_name(self):
        return None

    # 采购人名称
    def purchaser_name(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("采购代理机构信息")]

        result = re.findall('采购人信息名称：(.*?)地址', content)
        return result[0] if len(result) else ''

    # 采购联系人
    def purchaser_person(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("采购代理机构信息")]

        result = re.findall('项目联系人（询问）：(.*?)项目联系方式', content)
        return result[0] if len(result) else ''

    # 采购人地址
    def purchaser_address(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("采购代理机构信息")]

        result = re.findall('地址：(.*?)传真', content)
        return result[0] if len(result) else ''

    # 采购联系人对应联系方式
    def purchaser_contact(self):
        content = self.str[self.str.find("采购人信息"):self.str.find("采购代理机构信息")]

        result = re.findall('项目联系方式（询问）：(.*?)质疑联系人', content)
        return result[0] if len(result) else ''

    # 招标时间

    def bidding_time(self):
        return None

    # 招标代理名称
    def bidding_agent_name(self):
        agent_name = re.findall("采购代理机构信息名称：(.*?)地址：", self.str)
        return agent_name

    # 招标代理名称地址
    def bidding_agent_purchaser_address(self):
        content = self.str[self.str.find(
            "采购代理机构信息"):self.str.find("同级政府采购监督管理部门名称")]

        result = re.findall('地址：(.*?)传真', content)
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
            "采购代理机构信息"):self.str.find("同级政府采购监督管理部门名称")]

        result = re.findall('项目联系方式（询问）：(.*?)质疑联系人', content)
        return result[0] if len(result) else ''

    # 项目名称
    # def project_name(self, name):
    #     return name or None

    # 网站链接
    # def website_url(self):
    #     return None

    # note: 表格解析后的数据完全没特征可以抓取，所以这里准备抓取解析成文本之前的html，对 table 数据格式化，找对对应关系
    # pandas render_html 无效
    # playwright TODO

    # 产品
    def product(self):
        return None

    # 参数
    def parameter(self):
        return None

    # 单价
    def unit_price(self):
        return None

    # 最高限价
    def maximum_price(self):
        content = self.str[self.str.find("项目基本情况"):self.str.find("申请人的资格要求")]
        result = re.findall('最高限价（元）：(.*?)采购需求', content)
        result1 = re.findall('预算金额（元）：(.*?)最高限价', content)
        if (len(result)):
            if result[0] == '/':
                if (len(result1)):
                    return result1[0]
                else:
                    return ''
            return result[0]
        else:
            return ''

    # 预算
    def budget_price(self):
        content = self.str[self.str.find("项目基本情况"):self.str.find("申请人的资格要求")]
        result = re.findall('预算金额（元）：(.*?)最高限价', content)
        return result[0] if len(result) else ''

    # 中标金额
    def bid_amount(self):
        # 规则列表，任意一种匹配到了都算
        re_list = [
            "报价:(.*?)\(元",
            "投标总价:(.*?)\(元"
        ]
        result = ''
        for item in re_list:
            finded = re.findall(item, self.str)
            if finded:
                result = finded
                break

        return result

    # 中标单位
    def winning_bidder(self):
        # 中标结果和废标结果之间找
        content = self.str[self.str.find("中标结果"):self.str.find("废标结果")]

        tail = '公司'
        result = re.findall('\d\(元\)(.*)'+tail, content)
        if (len(result)):
            return result[0] + tail
        else:
            return ''

    def contractCode(self):
        # 合同编号：
        result = re.findall('合同编号：(.*?)二、合同名称', self.str)
        return result[0] if len(result) else ''

    def supplierContact(self):
        # 乙方联系方式：
        content = self.str[self.str.find("供应商（乙方）"):self.str.find("合同主体信息")]
        result = re.findall('联系方式：(.*?)六、', content)

        return result[0] if len(result) else ''

    def purchase_dead_line(self):
        # 采购截止时间
        result = re.findall('开标时间：(.*?)开标地点', self.str)
        return result[0] if len(result) else ''

    def mainSubjectInfo(self):
        # 主要标的信息
        content = self.str[self.str.find("主要标的信息"):self.str.find("合同金额")]
        name_result = re.findall('主要标的名称：(.*?)数量：', content)
        count_result = re.findall('标项(.*?)主要', content)

        # 构造和 jsondata 一样的数据格式

        result_list = []
        for item_index in range(len(name_result)):
            result_list.append({
                "mainSubjectName": name_result[item_index],
                "sectionNo": _trans(count_result[item_index])
            })

        # print(result_list)

        return result_list

    def project_name(self):
        re_list = [
            "标项名称:(.*?)数量",
            "标项名称：(.*?)数量"
        ]
        result = ''
        for item in re_list:
            finded = re.findall(item, self.str)
            if finded:
                result = finded
                break

        return result

    def project_name_race(self):
        result = re.findall('项目名称：(.*?)采购方式：', self.str)
        return result if len(result) else ''

    def project_count(self):
        result = re.findall('合同履约期限：(.*?)，', self.str)
        return result[0] if len(result) else ''
