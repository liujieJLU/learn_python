# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import re

#加载cookie文件登录贴吧类
class LoadCookie:
    def __init__(self,cookiesUrl):
        self.cookiesUrl = cookiesUrl
    def loadFile(self):
        # 创建MozillaCookieJar实例对象
        cookie = cookielib.MozillaCookieJar()
        # 读取cookies
        cookie.load(self.cookiesUrl,ignore_discard=True, ignore_expires=True)
        return cookie
        
#处理标签工具类
class Tool:
    # 取出img标签，7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    # 将换行标签替换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</P>')
    # 将表格制表<td>换为\t
    replaceTd = re.compile('<td>')
    # 把段落头换为\n加空格
    replacePara = re.compile('<p.*?>')
    # 把换行符或者双换行符替换为\n
    replaceBr = re.compile('<br><br>|<br>')
    # 将其他标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTd,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBr,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

#百度贴吧爬虫类
class BDTB:
 
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ,saveUrl,cookiesUrl):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.saveUrl = saveUrl
        self.tool = Tool()
        self.cookie = LoadCookie(cookiesUrl)
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie.loadFile()))
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None
    def getTitle(self):
        page=self.getPage(1)
        # 获取括号里的内容
        pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        # 使用re.search可以获取多个匹配项，result.group(1)取第一个匹配项
        result = re.search(pattern,page)
        if result:
            # print ""
            return result.group(1).strip()
        else:
            return None
    def getPageNum(self):
        page=self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
    # 直接保存全部楼层信息到文件中
    def getAllContent(self):
        i=0
        for p in range(1,int(self.getPageNum())+1):
            page = self.getPage(p)
            pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
            result = re.findall(pattern,page)
            contents=""
            file = open(self.saveUrl, 'a')
            for string in result:
                i +=1
                file.write(str(i)+"楼:==========================================================\n\t"+self.tool.replace(string.strip())+"\n")
                # print "   "+str(i)+":"+string.strip()
                # contents +=str(i)+":"+string.strip()
        file.close()
        
    # 返回每页的信息 
    def getContent(self,page):
        i=0
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        result = re.findall(pattern,page)
        contents=""
        for string in result:
            i +=1
            contents +=str(i)+"楼:==========================================================\n\t"+self.tool.replace(string.strip())+"\n"
        return contents
    def saveInfo(self,contents):
        file = open(self.saveUrl, 'a')
        file.write(contents)
        file.close()
# 目前的问题是爬取每一页的步骤没有显示，还未发现原因
    def startDemo(self):
        print "开始执行"
        pageNum = self.getPageNum()
        if pageNum == None:
            print "URL已经失效，请重试"
            return
        try:
            print "该帖子共有"+str(pageNum)+"页数据"
            for i in range(1,int(pageNum)+1):
                # print u"正在写入第页数据"
                print "正在写入第"+str(i)+"页数据"
                contents = self.getContent(self.getPage(i))
                self.saveInfo(contents)
        except Exception as e:
            print "写入异常，原因："+e.message


baseURL = 'https://tieba.baidu.com/p/5039021238'
fileUrl = 'D:/python/urliib/tieba2.txt'
cookiesUrl = 'D:/python/urliib/baidu_login.txt'
bdtb = BDTB(baseURL,0,fileUrl,cookiesUrl)
# print bdtb.getPage(1)
# print bdtb.getTitle()
# print bdtb.getPageNum()
# print bdtb.getAllContent()
# bdtb.saveInfo(bdtb.getPage(1))
bdtb.startDemo()