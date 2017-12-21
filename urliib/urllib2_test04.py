# import urllib2
# request = urllib2.Request('http://www.baicai.com')
# try urllib2.urlopen(request)
# except urllib2.URLErro,e:
# 	print e.reason
import urllib2  
req = urllib2.Request('http://www.baibai.com')
try: urllib2.urlopen(req)  
except urllib2.URLError, e:    
    print e.reason