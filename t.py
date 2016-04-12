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

def do_get(url, province):
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
						fd = open(tmp, 'w')
						fd.write(urllib2.urlopen(url).read())
						fd.close()
						print 'file:////c:/'+tmp,",",province,",",
				
				if txt.find("×") >= 0 and txt.find("亲本来源") < 0:
					tmp = txt.split("×")
					print tmp[0],",",tmp[1],",",
					continue
				print txt, ",",
			print

maps = {
	"http://www.ricedata.cn/variety/identified/nation_%d.htm":(26,"国家"),
	"http://www.ricedata.cn/variety/identified/vejd_%d.htm":(14, "浙江"),
	"http://www.ricedata.cn/variety/identified/fujm_%d.htm":(11, "福建"),

}
for k,v in maps.items():
	vv, pp = v
	for i in range(1, vv):
		url = k % i
		do_get(url, pp )

