from urllib2 import Request,urlopen,URLError,HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
request = Request(old_url)
response = urlopen(request)
print 'Old url :'+old_url
print 'Real url:'+response.geturl()