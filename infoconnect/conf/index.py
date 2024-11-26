
# 数据库配置
from datetime import date, timedelta

DB_HOST = '101.200.77.202'
DB_USER = 'infoconnect'
DB_PORT = '3306'
DB_PASSWORD = 'noNaanKAlnX8h1mx'
DB_DATABASE = 'infoConnect'


def format_day(days):
    return (date.today() - timedelta(days=days)).strftime('%Y-%m-%d')


# 数据字典
KEYWORD_DIC = {
    "教室": [],
    "智慧教室": ["智慧教育"],
    "多媒体教室": ["多媒体", "计算机教室"],
    "实训室": [],
    "专用教室": ["学科教室"],
    "学科教室": ["教室"],
    "阶梯教室": [],
    "微格教室": [],
    "创客教室": [],
    "智慧计算机教室": ["计算机教室", "智慧多媒体教室"],
    "中控": [],
    "网络中控": [],
    "中控主机": [],
    "中央控制器": ["一体机"],
    "集中控制管理系统": [],
    "控制面板": [],
    "融合管理终端": ["智能融合终端"],
    "智能集控管理终端": ["集控管理终端"],
    "物联网控制中心": [],
    "中央控制系统": [],
    "讲台": [],
    "讲桌": [],
    "讨论桌": [],
    "研讨桌": [],
    "实训桌": [],
    "演讲桌": [],
    "演讲台": [],
    "电子班牌": [],
    "智能信息展示屏": ["电子白板", "智慧大屏", "智能展示屏"],
    "智慧助教软件": [],
    "智慧校园管理融合平台": ["智慧校园", "智慧校园融合平台", "校园管理平台"]
}

keyword_list1 = [
    "教室",
    "智慧教室",
    "多媒体教室",
    "实训室",
    "专用教室",
    "学科教室",
    "阶梯教室",
    "微格教室",
    "创客教室",
    "智慧计算机教室"
]

keyword_list2 = [
    "中控",
    "网络中控",
    "中控主机",
    "中央控制器",
    "集中控制管理系统",
    "控制面板",
    "融合管理终端",
    "智能集控管理终端",
    "物联网控制中心",
    "中央控制系统"
]

keyword_list3 = [
    "讲台",
    "讲桌",
    "讨论桌",
    "研讨桌",
    "实训桌",
    "演讲桌",
    "演讲台"
]

keyword_list4 = [
    "电子班牌",
    "智能信息展示屏"
]

keyword_list5 = [
    "智慧助教软件"
]

keyword_list6 = [
    "智慧校园管理融合平台"
]

keyword_list_test = [
    "博物馆安保"
]

keyword_list_all = [element for lis in [keyword_list1, keyword_list2,
                                        keyword_list3, keyword_list4, keyword_list5, keyword_list6] for element in lis]

# 时间范围
# today, last_three_day, last_week, last_month, last_three_month, last_half_year, last_year
time_range_type = 'last_week'

# 地区 map
PLACE_MAP = {
    "ZHEJIANG": '0',  # '浙江',
    "BEIJING": '1',  # 北京',
    "HENAN": '2',  # '河南',
    "ANHUI": '3',  # '安徽',
    "SICHUAN": '4',  # '四川',
    "HUBEI": '5',  # '湖北',
    "HEBEI": '6',  # '河北',
    "SHANGHAI": '7',  # '上海',
    "SHANXI": "8",  # 陕西
}

ALLOWED_DOMAINS = [
    "zfcg.czt.zj.gov.cn",
    "zfcgmanager.czt.zj.gov.cn",
    "www.ccgp-beijing.gov.cn",
    "fwxt.czj.beijing.gov.cn",
    "www.ccgp-anhui.gov.cn",
    "www.ccgp-sichuan.gov.cn",
    "www.ccgp-hubei.gov.cn",
    "www.ccgp-hebei.gov.cn",
    "search.hebcz.cn",
    "www.zfcg.sh.gov.cn",
    'localhost'
]

# 来源配置
SOURCE_MAP = {
    # PLACE_MAP["ZHEJIANG"]: {
    #     'home_page_url': 'https://zfcg.czt.zj.gov.cn',
    #     'query_base_url': 'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results',
    #     'query_method': 'GET',
    #     'detail_base_url': 'https://zfcg.czt.zj.gov.cn/innerUsed_noticeDetails/index.html',
    #     'keyword_list': keyword_list_all
    # },
    # PLACE_MAP["BEIJING"]: {
    #     'home_page_url': 'http://www.ccgp-beijing.gov.cn',
    #     'query_base_url': 'http://fwxt.czj.beijing.gov.cn/was5/web/search',
    #     'query_method': 'GET',
    #     'detail_base_url': '',
    #     'keyword_list': keyword_list_all
    # },
    # PLACE_MAP["ANHUI"]: {
    #     'home_page_url': 'http://www.ccgp-anhui.gov.cn',
    #     'query_base_url': 'http://www.ccgp-anhui.gov.cn/front/search/category',
    #     'query_method': 'JSON_POST',
    #     'detail_base_url': '',
    #     'keyword_list': keyword_list_test
    # },
    PLACE_MAP["SICHUAN"]: {
        'home_page_url': 'http://www.ccgp-sichuan.gov.cn',
        'query_base_url': 'http://www.ccgp-sichuan.gov.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do',
        'query_method': 'GET',
        'detail_base_url': '',
        'keyword_list': keyword_list_all
    },
    # PLACE_MAP["HUBEI"]: {
    #     'home_page_url': 'http://www.ccgp-hubei.gov.cn',
    #     'query_base_url': 'http://www.ccgp-hubei.gov.cn:9040/quSer/search',
    #     'query_method': 'FORM_POST',
    #     'detail_base_url': '',
    #     'keyword_list': keyword_list_test
    # },
    # PLACE_MAP["HEBEI"]: {
    #     'home_page_url': 'http://www.ccgp-hebei.gov.cn',
    #     'query_base_url': 'http://search.hebcz.cn:8080/was5/web/search',
    #     'query_method': 'GET',
    #     'detail_base_url': '',
    #     'keyword_list': keyword_list_all
    # },
    PLACE_MAP["SHANGHAI"]: {
        'home_page_url': 'http://www.zfcg.sh.gov.cn',
        'query_base_url': 'http://www.zfcg.sh.gov.cn/front/search/category',
        'query_method': 'JSON_POST',
        'detail_base_url': '',
        'keyword_list': keyword_list_all
    },
}

# 查询关键词配置
DEFAULT_QUERY_MAP = {
    PLACE_MAP["ZHEJIANG"]: {
        'query_default_param': {
            "sourceAnnouncementType": "3004,4005,4006",
            "url": "notice",
            "isExact": 1,
            "pageNo": 1,
            "pageSize": 100,
            "pubDate": format_day(365),
            "endDate": date.today(),
        },
        'search_key': 'keyword',
    },
    PLACE_MAP["BEIJING"]: {
        'query_default_param': {
            "channelid": '212555',
            "searchscope": "doctitle",  # 按照标题精确查找
            "token": "",
            "orderby": "RELEVANCE",
            "timescopecolumn": "docRelTime",
            "perpage": "10",
            "timescope": "year"
        },
        'search_key': 'searchword'
    },
    PLACE_MAP["ANHUI"]: {
        'query_default_param': {
            "leaf": "0",
            "categoryCode": "ZcyAnnouncement4",
            "pageSize": "15",
            "pageNo": 1
        },
        'search_key': 'keyword'
    },
    PLACE_MAP["SICHUAN"]: {
        'query_default_param': {
            "noticeType": "00102",
            "selectTimeName": "noticeTime",
            "pageSize": 15,
            "currPage": 1
        },
        'search_key': 'title'
    },
    PLACE_MAP["HUBEI"]: {
        'query_default_param': {
            "queryInfo.type": "xmgg",
            "queryInfo.key": "",
            "queryInfo.jhhh": "",
            "queryInfo.fbr": "",
            "queryInfo.gglx": "中标（成交结果）公告",
            "queryInfo.cglx": "",
            "queryInfo.cgfs": "",
            "queryInfo.city": "湖北省",
            "queryInfo.qybm": "42????",
            "queryInfo.district": "全省",
            "queryInfo.cgr": "",
            "queryInfo.begin": "",
            "queryInfo.end": "",
            "queryInfo.pageNo": "1",
            "queryInfo.pageSize": "15"
        },
        'search_key': 'title'
    },
    PLACE_MAP["HEBEI"]: {
        'query_default_param': {
            "channelid": "240117",
            "lanmu": "zhbggAAAAAAAS",
            "syprovince": "0",
            "perpage": "50",
            "fstarttime": "2022-01-21",
            "fendtime": "2023-01-21"
        },
        'search_key': 'sydoctitle'
    },
    PLACE_MAP["SHANGHAI"]: {
        'query_default_param': {
            "categoryCode": "ZcyAnnouncement4",
            "pageNo": "1",
            "pageSize": "15",
            "publishDateBegin": "2022-01-20",
            "publishDateEnd": "2023-01-20",
        },
        'search_key': 'keyword'
    },
}

# all_keyword_lastweek
TASK1 = {
    "keyword_list": keyword_list_all,
    "time_range_type": "last_year",
    "isExact": "content",
    "TASK_CODE": '2023_1_14_1'
}

TASK2 = {
    "keyword_list": keyword_list_test,
    "time_range_type": "all",
    "isExact": "content",
    "TASK_CODE": 'sichuan_and_shanghai_winning_notice2'
}

#  对外导出的任务
TASK = TASK2
