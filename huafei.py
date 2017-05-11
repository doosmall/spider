#!/usr/bin/env python
# encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import urllib2
from bs4 import BeautifulSoup
import codecs

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "http://www.china-fertinfo.com.cn/viewccjg.aspx"



data = {
'__VIEWSTATE':'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',
'__EVENTTARGET':'pager1',
'__EVENTARGUMENT':3,
'__VIEWSTATEENCRYPTED':'',
'__EVENTVALIDATION':'zei/8+WcI0b2rXY9HjAY5nHmlL9KiFup8NSHxGTQaq/vihUN3A4N4EVqV5lhjJc99Y2SD61n5SnZZSSGfjM367X5Kmpdn9vYBxzcE/FxUWAW+FH7hKo3O+wlXowJT0U1yqmBmw==',
'txtgjz':'',
'txtqymc':'',
'txtjssj':'',
'txtkssj':'',
'pager1_input':2
}

cookie = {
    'Host': 'www.china-fertinfo.com.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://www.china-fertinfo.com.cn',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.china-',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cookie': 'validateNum=num=5933; sessionid=yhid=1541&yhzh=hfwz; AJSTAT_ok_times=2; ASP.NET_SessionId=vrtvax55ssaligbtnwfmnaej; safedog-flow-item=E55648C87755EA473970EC8F267C61B1',
}



def do_get(idx):
    data['__EVENTARGUMENT'] = idx
    print 'do get ', url, idx
    req = urllib2.Request(url = url, data = urllib.urlencode(data),  headers=cookie)
    res = urllib2.urlopen(req)
    return res.read()


import time

fd = open("res.html", "w")
for i in range(7795):
    time.sleep(1)
    try:
        res = do_get(i)
    except:
        continue
    bs = BeautifulSoup(res, from_encoding="gb2312")
    for table in bs.find_all('table',id='GridView2'):
        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):
                tmp = td.text.lstrip().rstrip()
                fd.write(tmp)
                fd.write("\t")
            fd.write("\n")
fd.close()
