#-*- coding:utf-8 -*-
import os
import requests
from ReadJson import read_config
from RequestsHeader import req_headers


class SendNotify(object):
    def __init__(self, message):
        self.message = message

    def sendTo(self):
        tg_dict = read_config()
        if tg_dict:
            tg_chat = tg_dict['tg-chat']
        else:
            print u"配置文件不存在"
        try:
            requests.post(tg_chat, json={"text": self.message})
        except:
            print u"网络访问失败! "
