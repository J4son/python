import httplib

headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain","header-rootme-admin":"admin"}


conn = httplib.HTTPConnection("challenge01.root-me.org")
conn.set_debuglevel(9)
conn.request("GET","/web-serveur/ch5/",str(headers))
#conn.request("GET","http://challenge01.root-me.org/web-serveur/ch2  HTTP/1.0",str(headers))
conn.endheaders

res = conn.getresponse()
print (res.status,res.reason,res.getheaders())



