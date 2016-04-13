#!/usr/bin/python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import urllib2
from bs4 import UnicodeDammit as UD
import codecs
import encodings
encodings.aliases.aliases['gb2312'] = 'gb18030'

look  = codecs.lookup("windows-1252")

h = {}

def do_get(url, p, province):
	content =urllib2.urlopen(url).read()
	#bs = BeautifulSoup(content, from_encoding = "windows-1252")
	bs = BeautifulSoup(content)
	#print bs.original_encoding
	tables = bs.find_all("table")
	for table in tables: 
		try:
			if int(table['cellpadding']) != 2:
				continue
		except:
			continue
		trs= table.find_all("tr")
		for tr in trs:
			if str(tr).find("序号") >= 0:
				continue
			tds = tr.find_all("td")
			for td in tds:
				if len(td.text) <= 0:
					continue
				txt = td.text
				ass = td.find_all("a")
				if ass is not None:
					for a in ass:
						tmp = a['href'].replace('../','')
						prefix = 'http://www.ricedata.cn/variety/'
						url = prefix+tmp
						a, b = tmp.split('/')
						file = '%s/%s/%s' % (a, p, b)
						fd = open(file, 'w')
						fd.write(urllib2.urlopen(url).read())
						fd.close()
						print 'file:////c:/'+file,",",province,",",
				
				if txt.find("×") >= 0 and txt.find("亲本来源") < 0:
					tmp = txt.split("×")
					print tmp[0],",",tmp[1],",",
					continue
				print txt, ",",
			print

maps = {
	"http://www.ricedata.cn/variety/identified/nation_%d.htm":(26,'nation', "国家"),
	"http://www.ricedata.cn/variety/identified/vejd_%d.htm":(14, 'zhejiang', "浙江"),
	"http://www.ricedata.cn/variety/identified/fujm_%d.htm":(11, 'fujiang', "福建"),
	"http://www.ricedata.cn/variety/identified/jdxi_%d.htm":(22, 'jiangxi', "江西"),
	"http://www.ricedata.cn/variety/identified/jdsu_%d.htm":(13, 'jiangsu', "江苏"),
	"http://www.ricedata.cn/variety/identified/anhv_%d.htm":(13, 'anhui', "安徽"),
	"http://www.ricedata.cn/variety/identified/uhhl_%d.htm":(5, 'shanghai', "上海"),
	"http://www.ricedata.cn/variety/identified/ujds_%d.htm":(3, 'shandong', "山东"),
	"http://www.ricedata.cn/variety/identified/hlj_%d.htm":(9, 'heilongjiang', "黑龙江"),
	"http://www.ricedata.cn/variety/identified/jxln_%d.htm":(13, 'jilin', "吉林"),
	"http://www.ricedata.cn/variety/identified/lcny_%d.htm":(10, 'liaoning', "辽宁"),
	"http://www.ricedata.cn/variety/identified/hebz_%d.htm":(3, 'hebei', "河北"),
	"http://www.ricedata.cn/variety/identified/nmg_%d.htm":(3, 'neimenggu', "内蒙古"),
	"http://www.ricedata.cn/variety/identified/ujxi_%d.htm":(2, 'shanxi', "山西"),
	"http://www.ricedata.cn/variety/identified/tmjn_%d.htm":(4, 'tianjin', "天津"),
	"http://www.ricedata.cn/variety/identified/bzjy_%d.htm":(2, 'beijing', "北京"),
	"http://www.ricedata.cn/variety/identified/sjxi_%d.htm":(4, 'sanxi', "陕西"),
	"http://www.ricedata.cn/variety/identified/gjsu_%d.htm":(2, 'gansu', "甘肃"),
	"http://www.ricedata.cn/variety/identified/nyxw_%d.htm":(4, 'ningxia', "宁夏"),
	"http://www.ricedata.cn/variety/identified/xnjd_%d.htm":(3, 'xinjiang', "新疆"),
	"http://www.ricedata.cn/variety/identified/hunj_%d.htm":(22, 'hunan', "湖南"),
	"http://www.ricedata.cn/variety/identified/henj_%d.htm":(6, 'henan', "河南"),
	"http://www.ricedata.cn/variety/identified/hubz_%d.htm":(11, 'hubei', "湖北"),
	"http://www.ricedata.cn/variety/identified/gdds_%d.htm":(21, 'guangdong', "广东"),
	"http://www.ricedata.cn/variety/identified/gdxi_%d.htm":(22, 'guangxi', "广西"),
	"http://www.ricedata.cn/variety/identified/hlnj_%d.htm":(8, 'hainan', "海南"),
	"http://www.ricedata.cn/variety/identified/siir_%d.htm":(13, 'sichuan', "四川"),
	"http://www.ricedata.cn/variety/identified/ypnj_%d.htm":(11, 'yunnan', "云南"),
	"http://www.ricedata.cn/variety/identified/gvvb_%d.htm":(10, 'guizhou', "贵州"),
	"http://www.ricedata.cn/variety/identified/isqy_%d.htm":(6, 'chongqing', "重庆"),
}
import os
for k,v in maps.items():
	vv, p,  pp = v
	try:
		os.mkdir('varis/%s' % p )
	except:
		pass
	for i in range(1, vv):
		url = k % i
		do_get(url, p, pp )

