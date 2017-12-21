# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.1
#   作者：Kelvin
#   日期：2016-05-21
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#---------------------------------------
import urllib2,string
#定义贴吧爬虫函数
def tieba(url,start,end):
    #从start到end+1进行循环
    for i in range(start,end+1):
        fName=string.zfill(i,5)+'.html'#将文件命名为六位的带有序号的html文件
        print '正在下载第'+str(i)+'个文件，并将其转存为'+fName
        file=open(fName,'w+')
        #获取内容并进行解析
        response=urllib2.urlopen(url+str(i)).read()
        #写入文件
        file.write(response)
        #关闭文件
        file.close()
#--------------------------------------------------
#获取用户输入
bdurl=str(raw_input(u'请输入帖子的URL，不包含pn之后的数字\n'))
start=int(raw_input(u'请输入起始页码\n'))
end=int(raw_input(u'请输入终止页码\n'))

#调用函数
tieba(bdurl,start,end)