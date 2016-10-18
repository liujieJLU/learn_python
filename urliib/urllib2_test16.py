# -*- coding:utf-8 -*-

#-------------
#	程序：百度贴吧爬虫
# 	版本：0.1
# 	作者：liujie
# 	日期：2016-9-14 14:45:30
# 	语言：Python 2.7
# 	操作：输入带分页的地址去掉最后面的数字，设置起始页数和终点页数
# 	功能下载页码内所有文件并存储为html文件
# ---------------------
import string,urllib

#定义百度函数
def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page+1):
		sName = string.zfill(i,5)+'.html'	#自动填充成六位的文件名
		print'正在下载'+str(i) + '个网页，并将其存储为' + sName+'.......'
		f = open(sName,'w+')
		print url+str(i)
		m = urllib.urlopen(url+str(i)).read()
		f.write(m)
		f.close()

#--------------在这里输参数-----------------

# 这是吉林大学百度贴吧某个帖子地址
bdurl  = 'http://tieba.baidu.com/p/4547484171?pn='
begin_page = 1
end_page = 5
# bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
# begin_page = int(raw_input(u'请输入开始的页数； \n'))
# end_page = int(raw_input(u'请输入终点的页数：\n'))
#---------输入参数--------------

baidu_tieba(bdurl,begin_page,end_page)