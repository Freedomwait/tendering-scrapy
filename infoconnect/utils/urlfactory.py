from urllib.parse import urlencode


class UrlFactory:
    def __init__(self, base_url, query_dict):
        self.base_url = base_url
        self.query_dict = query_dict

    def build(self):
        query = urlencode(self.query_dict)
        url = '?'.join([self.base_url, query])
        return url
    
    def build_url_list(self):
        return None;




# print(targetUrl.build_url())
