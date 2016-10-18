# -*- coding: utf-8 -*-  
# import urllib2  
# my_url = 'http://www.google.cn'  
# response = urllib2.urlopen(my_url)  
# redirected = response.geturl() == my_url  
# print redirected
  
# my_url = 'http://rrurl.cn/b1UZuP'  
# response = urllib2.urlopen(my_url)  
# redirected = response.geturl() == my_url  
# print redirected 

# import urllib2
# class RedirectHandler(urllib2.HTTPRedirectHandler):
# 	def http_error_301(self,req,fp,code,msg,headers):
# 		print "301"
# 		pass
# 	def http_error_302(self,req,fp,code,msg,headers):
# 		print "303"
# 		pass
# opener = urllib2.build_opener(RedirectHandler)
# opener.open("http://rrurl.cn/b1UZuP")


# import urllib2
# import cookielib
# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open('http://www.baidu.com')
# for item in cookie:
# 	print 'Name='+item.name
# 	print 'Value='+item.value


# import urllib2
# try:
# 	response = urllib2.urlopen('http://bbs.csdn.net/why')
# except urllib2.HTTPError, e:
# 	print e.code

# import urllib2
# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler,httpsHandler)
# urllib2.install_opener(opener)
# response  = urllib2.urlopen('http://www.baidu.com')

 
import urllib  
import urllib2  
postdata=urllib.urlencode({  
    'username':'汪小光',  
    'password':'why888',  
    'continueURI':'http://www.verycd.com/',  
    'fk':'',  
    'login_submit':'登录'  
})  
req = urllib2.Request(  
    url = 'http://secure.verycd.com/signin',  
    data = postdata  
)  
result = urllib2.urlopen(req)  
print result.read()
