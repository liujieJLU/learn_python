#-*-coding:utf-8-*-
import urllib2
#创建密码管理器
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

#添加用户名和密码

top_level_url = "http://example.com/foo/"

#如果知道realm，我们可以使用它代替''None''
#passwrod_mgr.add_password(None,top_url,username,password)

password_mgr.add_password(None,top_level_url,'why','123')

#创建新的handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

#创建opener

opener = urllib2.build_opener(handler)

a_url = 'http://baidu.com'

#使用opener获得一个url
content_steam=opener.open(a_url)
print content_steam
urllib2.install_opener(opener)
