import urllib2
import urllib

req = urllib2.Request('http://bbs.csdn.net/callmewhy')
try:
	response=urllib2.urlopen(req)
except urllib2.URLError , e:
	print e.code

