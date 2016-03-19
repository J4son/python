import http.client

resultat = http.client.HTTPConnection("www.secu-info.net")
resultat.set_debuglevel(9)
resultat.request("Get index.html")
