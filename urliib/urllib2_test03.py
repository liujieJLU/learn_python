import urllib
import urllib2
url = 'http://www.someserver.com/register.cgi'
values={'name':'why','location':'SDU','language':'Python'}
print urllib.urlencode(values)
data = urllib.urlencode(values)
request  = urllib2.Request(url,data)
response = urllib2.urlopen(request)
the_page = response.read()
# name=Somebody+Here&language=Python&location=Northampton    
# url = 'http://www.example.com/example.cgi'    
# full_url = url + '?' +values  
  
# data = urllib2.open(full_url)