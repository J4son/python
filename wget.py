import urllib,re,os

fichier = open('/Users/brur/Desktop/bruno.txt','w')
h = urllib.urlopen('http://207.235.20.29/DeviceInformation')
print h.read()
for line in h.readlines():
    fichier.write(line)
    if (re.search("Serial",line)):
        print "\n",line,"\t OK j\'ai trouver"
        fichier.write("coucou")
    









