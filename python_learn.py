import httplib,urllib2


httplib.HTTPConnection.debuglevel = 1
request = urllib2.Request('http://challenge01.root-me.org//web-serveur/ch2/')
opener = urllib2.build_opener()
feeddata = opener.open(request).read()                        
print feeddata

"""tableau=('0','0','0','0','0','0','1','1','1','1','1','1')
tab = [""]
tab = tableau


#for i in range(len(tableau)):
     #tab[i] = tableau
     #print i, ":_____________:" ,tab[i]

for j in range(len(tab)):
     resultat = int(tab[j])
"""
