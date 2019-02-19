
#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import os
import time
from io import open
import linecache
from SendNotify import SendNotify
from VisitPage import VisitPage
from ReadJson import read_config


def script(urls, tg_chat):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    for url in urls:
        url = url.replace('https://', '')
        filename = 'logs/%s/%s.txt' % (url.replace('http://', ''), time.strftime(
            "%Y-%m-%d", time.localtime(time.time())))
        # vist page
        url_result = VisitPage(url)
        status = url_result.visit()
        # send notify
        if status == '-1' or status == '500' or status == '502': # 502 & 500
             # record in local
            path_exit = os.path.exists(filename)
            if path_exit:
                file = open(filename, 'r', encoding='utf-8')
                linecount = len(file.readlines())
                data = linecache.getline(filename, linecount)
                file.close
                if data == '':
                    print u"empty file"
                else:
                    explode = data.split('-----')
                    if explode[2] == '200\n' or data == '\n':
                        message = u"Website:%s no open %s" % (url, now_time)
                        send_notify = SendNotify(message)
                        send_notify.sendTo()
            else:
                print u"File no exit"
                # TODO 
                message = u"Website:%s no open %s" % (url, now_time)
                send_notify = SendNotify(message)
                send_notify.sendTo()
        else:
            # record in local
            path_exit = os.path.exists(filename)
            if path_exit:
                file = open(filename, 'r', encoding='utf-8')
                linecount = len(file.readlines())
                data = linecache.getline(filename, linecount)
                file.close
                if data == '':
                    print u"empty file"
                else:
                    explode = data.split('-----')
                    if explode[2] == '-1\n' or explode[2] == '500\n' or explode[2] == '502\n':
                        message = u"Website:%s on %s restore" % (url, now_time)
                        send_notify = SendNotify(message)
                        send_notify.sendTo()
                    else:
                        print u"End Record %s" % (explode[2])
            else:
                print u"File no exit"
        path_exit = os.path.exists('logs/%s' % url.replace('http://', ''))
        if path_exit == False:
            os.mkdir('logs/%s' % url.replace('http://', '')) 
        data = '\n' + url + '-----' + time.strftime("%H:%M:%S", time.localtime(time.time())) + '-----' + status
        file = open(filename, 'a', encoding='utf-8')
        file.write(data)
        file.close

if __name__ == "__main__":
    config_dict = read_config()
    if config_dict:
        urls = config_dict['urls']
        tg_chat = config_dict['tg-chat']
    else:
        print u"File no exit"

    # check
    while 1:
        script(urls, tg_chat)
        time.sleep(config_dict['time_interval_num'])
        linecache.clearcache()
