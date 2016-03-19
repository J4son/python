import urllib2,lxml
from lxml import etree
chemin = "/Users/brur/Desktop/00-DHC/ive-export.xml"
fichier = open(chemin,"r")
parser = lxml.etree.XMLParser()
fichier_xml = lxml.etree.parse(fichier,parser)
root = fichier_xml.getroot()


for element in root.iterdescendants():
    print element.tag,":",element.text
