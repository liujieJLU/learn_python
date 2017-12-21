#-*-coding:utf-8-*-
import urllib
import urllib2
import cookielib

fileName = 'baidu_login.txt'
#声明一个MozillaCookieJar 对象实例来保存cookie,之后写入文件
cookie = cookielib.MozillaCookieJar(fileName)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
	'userName':'1836698655@qq.com',
	'password':'liujie6666228'
	})

loginUrl='http://tieba.baidu.com/f/user/passport'
#模拟登陆把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
bauduUrl = 'http://tieba.baidu.com/p/4865601724?pn=2'
result = opener.open(bauduUrl)
print result.read()

