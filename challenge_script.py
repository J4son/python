import cookielib, urllib, urllib2

login = 'daytona675'
password = 'espace'

# On active le support des cookies pour urllib2
cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

# On envoie login/password au site qui nous renvoie un cookie de session
values = {'user':login, 'passwrd':password }
data = urllib.urlencode(values)
request = urllib2.Request("http://www.newbiecontest.org/forums/index.php?action=login2", data)
url = urlOpener.open(request)  # Notre cookiejar reçoit automatiquement les cookies
page = url.read(500000)

# On s'assure qu'on est bien logue en verifiant la présence du cookie "id"
if not 'PHPSESSID' in [cookie.name for cookie in cookiejar]:
    raise ValueError, "Echec connexion avec login=%s, mot de passe=%s" % (login,password)

print "Nous sommes connecte !"

# Maintenant on fait une autre requete sur le site avec notre cookie de session.
# (Notre urlOpener utilise automatiquement les cookies de notre cookiejar)
url = urlOpener.open('http://www.newbiecontest.org/epreuves/prog/prog1.php')
page2= url.read(200000)



url = urlOpener.open('http://www.newbiecontest.org/epreuves/prog/verifpr1.php?solution=' + page2.split(": ")[1])
page3= url.read(200000)
