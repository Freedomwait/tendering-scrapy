# # -*- coding: utf-8 -*-
# from scrapy.selector import Selector
# import scrapy
# body = '''<p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">根据《中华人民共和国政府采购法》等有关规定，浙江省地理信息中心就地物光谱仪进行公开招标，欢迎国内合格的供应商前来投标。</span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">一．招标项目编号:&nbsp;</span></strong><span style="line-height: 24px; font-family: 宋体;"></span>HZYX-SD-17127GK<span style="line-height: 24px; font-family: 宋体;"></span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">二．采购组织类型：</span></strong><span style="line-height: 24px; font-family: 宋体;"></span>分散采购委托代理<span style="line-height: 24px; font-family: 宋体;"></span></p><p style="line-height: 24px; white-space: normal;"><strong style="white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">三．招标项目概况：</span></strong></p><p style="line-height: 24px; white-space: normal;"><strong style="white-space: normal;"><span style="line-height: 24px; font-family: 宋体;"></span></strong></p><table class="needChange" style="border: 1px solid rgb(228, 230, 231); border-image: none; width: 100%; text-align: center; border-collapse: collapse; background-color: white;" cellspacing="0" cellpadding="0"><thead><tr class="firstRow"><th style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none; background-color: rgb(245, 245, 245);" contenteditable="false">序号</th><th style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none; background-color: rgb(245, 245, 245);" contenteditable="false">项目名称</th><th style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none; background-color: rgb(245, 245, 245);" contenteditable="false">数量</th><th style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none; background-color: rgb(245, 245, 245);" contenteditable="false">单位</th><th style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none; background-color: rgb(245, 245, 245);" contenteditable="false">预算金额</th><th style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none; background-color: rgb(245, 245, 245);" contenteditable="false">简要规格描述</th><th style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none; background-color: rgb(245, 245, 245);" contenteditable="false">备注</th></tr></thead><tbody><tr><td style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none;"><div>1</div></td><td style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none;"><div>地物光谱仪</div></td><td style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none;"><div>1</div></td><td style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none;"><div>套</div></td><td style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none;"><div>70.0000万元</div></td><td style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none;"><div>详见第三章项目技术规范和服务要求</div></td><td style="padding: 5px; border: 1px solid rgb(221, 221, 221); border-image: none;"><div>允许采购进口</div></td></tr></tbody></table><p style="line-height: 24px; white-space: normal;"><span style="text-indent: 36px; font-family: 宋体;">（除备注外其他为必填项）</span><br></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">四．投标供应商资格要求:</span></strong></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;">（1）符合《中华人民共和国政府采购法》第二十二条对投标主体的要求。投标人应具有独立承担民事责任的能力；具有良好的商业信誉和健全的财务会计制度；具有履行合同所必需的设备和专业技术能力；有依法缴纳税收和社会保障资金的良好记录；参加政府采购活动前三年内，在经营活动中没有重大违法记录。\n（2）本项目不接受联合体投标。</p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">五．招标文件的报名/发售时间、地址、售价:</span></strong></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 黑体;">1</span><span style="line-height: 24px; font-family: 黑体;">．报名/发售时间：2017-05-03</span><span style="line-height: 24px; font-family: 宋体;">至2017-05-12(双休日及法定节假日除外)</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">上午：09:00-11:30；下午：13:30-17:00</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 黑体;">2</span><span style="line-height: 24px; font-family: 黑体;">．报名/发售地址：</span>杭州意信招标代理有限公司（杭州市天目山路170号，西湖数源软件园，17号楼5层509室）<span style="line-height: 24px; font-family: 宋体;"></span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 黑体;">3</span><span style="line-height: 24px; font-family: 黑体;">．标书售价(元)：</span><span style="line-height: 24px; font-family: 宋体;">每本<strong><span style="line-height: 24px;"></span></strong>400（售后不退）</span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">六．投标截止时间：2017-05-23 14:00:00</span></strong></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">七．投标地址：<strong><span style="line-height: 24px;"></span></strong></span></strong>杭州市天目山路170号，西湖数源软件园，17号楼1层101会议室<span style="line-height: 24px; font-family: 宋体;"></span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">八．开标时间：</span></strong><strong><span style="line-height: 24px; font-family: 宋体;"></span></strong>2017-05-23 14:00:00<span style="line-height: 24px; font-family: 宋体;"></span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">九</span></strong><strong><span style="line-height: 24px; font-family: 宋体;">．开标地址</span></strong><span style="line-height: 24px; font-family: 宋体;">：<strong><span style="line-height: 24px;"></span></strong>杭州市天目山路170号，西湖数源软件园，17号楼1层101会议室</span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">十．投标保证金：</span></strong></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">投标保证金</span><span style="line-height: 24px; font-family: 黑体;">(</span><span style="line-height: 24px; font-family: 黑体;">元)</span><span style="line-height: 24px; font-family: 宋体;">：<strong><span style="line-height: 24px;"></span></strong>标项一: 12000.00元。 </span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">交付方式：<strong><span style="line-height: 24px;"></span></strong>于2017年5月19日下午16:00时前以电汇、网银的形式交纳至杭州意信招标代理有限公司并确认到帐</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">收款单位（户名）：杭州意信招标代理有限公司</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">开户银行：&nbsp;<strong><span style="line-height: 24px;"></span></strong>中国工商银行杭州国际花园支行</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">银行账号：<strong><span style="line-height: 24px;"></span></strong>1202 0523 1990 0022 431</span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="line-height: 24px; font-family: 宋体;">十一．其他事项：</span></strong></p><p style="line-height: 24px; text-indent: 28px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">1</span><span style="line-height: 24px; font-family: 宋体;">．供应商认为采购文件使自己的权益受到损害的，可以自收到采购文件之日（发售截止日之后收到采购文件的，以发售截止日为准）或者采购文件公告期限届满之日（招标公告为公告发布后的第6个工作日）起7个工作日内，以书面形式向采购人和采购代理机构提出质疑。质疑供应商对采购人、采购代理机构的答复不满意或者采购人、采购代理机构未在规定的时间内作出答复的，可以在答复期满后十五个工作日内向同级政府采购监督管理部门投诉。</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">2</span><span style="line-height: 24px; font-family: 宋体;">．投标人购买标书时应提交的资料：&nbsp;<strong><span style="line-height: 24px;"></span></strong>（1）有效的营业执照副本复印件、税务登记证复印件、社保登记证复印件、法人代表授权书、被授权人身份证复印件（均须加盖单位公章），杭外潜在供应商可将上述材料连同标书款缴纳凭证（付款信息见“十、投标保证金”）传真或电子邮件（hzyxzbdl@sina.com）至招标代理机构，并联系报名。\n（2）投标单位名称、地址、联系人、联系电话，公司开户行名称、帐号；\n（3）潜在供应商可在浙江政府采购网http://www.zjzfcg.gov.cn进行免费注册，成为浙江政府采购正式注册入库供应商，具体详见浙江政府采购网供应商注册要求；\n（4）招标文件发售截止时间之后潜在供应商仍然允许获取招标文件。但该供应商如对招标文件有疑问应按招标文件规定的询疑时间前提出，逾期提出的，招标组织机构可以不予受理、答复。</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">3. &nbsp;</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="line-height: 24px; font-family: 宋体;">4</span><span style="line-height: 24px; font-family: 宋体;">．</span></p><p style="line-height: 24px; white-space: normal;"><strong><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">十二．联系方式</span></strong></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">1</span><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">、采购代理机构名称：杭州意信招标代理有限公司</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">联系人：曹海英、范文晖</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">联系电话：0571- 88219719，87211505</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">传真：0571-87211507</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">地址：杭州市天目山路176号，西湖数源软件园，17号楼509室</span></p><p style="line-height: 24px; text-indent: 32px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">2</span><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">、采购人名称：浙江省地理信息中心</span></p><p style="line-height: 24px; text-indent: 32px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;"></span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">联系人：楼敞</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">联系电话：0571-88089137</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">传真：</span></p><p style="line-height: 24px; text-indent: 36px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">地址：</span></p><p style="line-height: 24px; text-indent: 32px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">3</span><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">、同级政府采购监督管理部门名称：浙江省财政厅政府采购监管处</span><br></p><p style="line-height: 24px; text-indent: 32px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">联系人：</span></p><p style="line-height: 24px; text-indent: 32px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">监督投诉电话：0571-87055741</span></p><p style="line-height: 24px; text-indent: 32px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">传真：</span></p><p style="line-height: 24px; text-indent: 32px; white-space: normal;"><span style="color: rgb(0, 32, 96); line-height: 24px; font-family: 宋体;">地址：</span></p><p style=\'font-size\' class=\'fjxx\'>附件信息：</p>'''

# selector = Selector(text=body).xpath('//body')
# list = []
# for s in selector:
#     if s.xpath('/node()').get() is not None and s.xpath("./style") is None:
#         # print('selector: ', s)
#         # 过滤 style 标签
#         list.append(''
#                     .join(s.xpath('string(.)').get())
#                     .replace('\n', '')
#                     .replace('\t', '')
#                     .replace('\u3000', '')
#                     .replace('\xa0', '')
#                     .replace(' ', '')
#                     .strip())
# result = ''.join(list)

# print(result)

# rows_body = ['序号', '标项名称', '标的名称', '品牌', '数量', '单价(元)', '规格型号', '1', '永嘉县2022年“温馨教室”工程学校新风采购-1', '吊装式单体双向流新风', '北京米微环保科技有限公司', '758', '3915', '米微、XD-ZS-800-V1;设备费用（含安装）：2728800元；1年维保费：238770元', '2', '永嘉县2022年“温馨教室”工程学校新风采购-2', '壁挂式双向流新风机', '上海士诺净化科技有限公司', '486', '2371', '士诺、TSX500AS；设备费用（含安装）：917568元；1年维保费用：234738元。']

# # print(int(len(row_body) / 7))
# # 全7个 是头部
# # 后面 是多余的列

# body_header = []
# items = int(len(rows_body) / 7)
# n_index = rows_body.index("品牌")
# brand_name = rows_body[n_index + 7]

# _result = []
# if items > 2:
#     for item in range(items):
#         if item > 0:
#             _result.append(rows_body[n_index + 7 * (item)])
#         # brand_name = rows_body[n_index + 7]

# print(_result)


# rows_body = ['序号', '中标（成交）金额（元）', '中标供应商名称', '中标供应商地址', '1', '① 新风机设备、安装总价:3029400(元),② 6次维护保养费:758000(元),本项目的投标总报价（①+②）:3787400(元)', '杭州卡丽智能科技股份有限公司',
#              '浙江省杭州市余杭区余杭街道天目山西路360号9幢302室', '2', '① 新风机设备、安装总价:1506600(元),② 6次维护保养费:376650(元),本项目的投标总报价（①+②）:1883250(元)', '浙江金海高科股份有限公司', '浙江省诸暨市应店街镇工业园区']


# items = int(len(rows_body) / 4)
# _result = []
# n_index = -1

# for index in range(len(rows_body)):
#     if("中标（成交）金额" in rows_body[index]):
#         n_index = index


# if items > 2:
#     for item in range(items):
#         if item > 0:
#             if(n_index != -1):
#                 _result.append(rows_body[n_index + 4 * (item)])

# print(_result)
def parse_table(rows_body, col_number, key):
        col = col_number
        _result = []
        try:
            n_index = -1
            for index in range(len(rows_body)):
                if(key in rows_body[index]):
                    n_index = index
                    break
            # n_index = rows_body.index(key)
            # 多个标的情况
            items = int(len(rows_body) / col)
            if items > 2:
                for item in range(items):
                    if item > 0 and n_index != -1 and n_index + col * item + 1 < len(rows_body):
                        print('n_index + col * item')
                        print(f'{len(rows_body)}')
                        print(n_index + col * item)
                        _result.append(rows_body[n_index + col * item])
            else:
                if n_index + col < len(rows_body):
                    _result = rows_body[n_index + col]

        except ValueError:
            print(f"无{key}")
        
        return _result