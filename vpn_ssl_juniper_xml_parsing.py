import lxml,os,sys,datetime,subprocess,glob
from lxml import etree

parser = lxml.etree.XMLParser()
fichier = open("/Users/brur/Desktop/ive-export.xml","r")

if not fichier:
	print ("impossible d'ouvrir le fichier")
	sys.exit(2)

fichier_xml = lxml.etree.parse(fichier,parser)
root = fichier_xml.getroot()

for element in root.iterdescendants(tag="{http://xml.juniper.net/ive-sa/6.5R9}users"):
        for elem in  element.iterdescendants():
                if elem.tag == "{http://xml.juniper.net/ive-sa/6.5R9}rule":
                        print elem.text


        
                

"""        
for element in root.iterdescendants():
	if element.tag == "ServerName":
                print("%s - %s" % (element.tag, element.text))
		servername.append((element.tag, element.text))
        elif element.tag == "Status":
                print("%s - %s" % (element.tag, element.text))
		status.append((element.tag, element.text))
		if element.text <> "SUCCESS":
			print ("Erreur de sauvegarde !!!")
			sys.exit(2)
        elif element.tag == "ComponentName":
                print("%s - %s" % (element.tag, element.text))

sys.exit(0)
"""
