from urllib2 import Request,urlopen,URLError,HTTPError

req = Request('httP://bbs.csdn.net/callmewhy')
try:
	response = urlopen(req)
except HTTPError , e:
	print 'The server couldn\'t fulfill the request.'
	print 'Error code :',e.code
except URLError,e:
	print 'We failed to each a server.'
	print 'Reason :',e.code
else:
	print 'no exception was raised.'
finally:
	pass