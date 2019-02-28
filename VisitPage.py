import sys
import requests
from RequestsHeader import req_headers
import urllib3

class VisitPage(object):
    def __init__(self, url):
        self.url = url

    def visit(self):
        try:
            urllib3.disable_warnings()
            res = requests.get(self.url, verify=False, headers=req_headers,
                               allow_redirects=True)
            code = res.status_code
            return str(code)
        except Exception as e:
            return '-1'
