import json
import math
from urllib.parse import parse_qs, urlparse
from infoconnect.utils.detail.anhui import anhui_result_detail
from infoconnect.utils.detail.beijing import beijing_result_detail
from infoconnect.utils.detail.hebei import hebei_result_detail
from infoconnect.utils.detail.hubei import hubei_result_detail
from infoconnect.utils.detail.shanghai import shanghai_result_detail
from infoconnect.utils.detail.sichuan import sichuan_result_detail
from infoconnect.utils.detail.zhejiang import zhejiang_result_detail
from infoconnect.utils.re.bj import Re_bj
from scrapy.selector import Selector
from infoconnect.conf.index import PLACE_MAP, SOURCE_MAP
from infoconnect.utils.urlfactory import UrlFactory
from infoconnect.utils.nodeparse import NodeParse


def parse_result_detail(spider, response):
    source_key = response.meta["source_key"]
    spider.logger.debug('parse_result_detail: source_key')
    spider.logger.debug(source_key)
    if source_key == PLACE_MAP["ZHEJIANG"]:
        return zhejiang_result_detail(spider, response)
    elif source_key == PLACE_MAP["BEIJING"]:
        return beijing_result_detail(spider, response)
    elif source_key == PLACE_MAP["ANHUI"]:
        return anhui_result_detail(spider, response)
    elif source_key == PLACE_MAP["SICHUAN"]:
        return sichuan_result_detail(spider, response)
    elif source_key == PLACE_MAP["HUBEI"]:
        return hubei_result_detail(spider, response)
    elif source_key == PLACE_MAP["HEBEI"]:
        return hebei_result_detail(spider, response)
    elif source_key == PLACE_MAP["SHANGHAI"]:
        return shanghai_result_detail(spider, response)

    pass
