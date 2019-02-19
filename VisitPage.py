import sys
import requests
from RequestsHeader import req_headers


class VisitPage(object):
    def __init__(self, url):
        self.url = url

    def visit(self):
        try:
            res = requests.get(self.url, headers=req_headers,
                               allow_redirects=True)
            code = res.status_code
            return str(code)
        except:
            return '-1'
