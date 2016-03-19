
#fichier = xml.etree.ElementTree.parse(document)


import xml,os,sys,datetime
from xml.etree.ElementTree import XMLTreeBuilder
document = "/Users/brur/Desktop/2011-07-28-02-00-00_drfComponent.xml"
#document = "/Users/brur/Documents/sauv.xml"
#document = "/Users/brur/Documents/2011-05-19-03-01-25_drfComponent.xml"
fichier = xml.etree.ElementTree.parse(document)

Server_Name = fichier.findall("FeatureObject/vServerObject/ServerObj/ServerName")
Server_Status = fichier.findall("FeatureObject/vServerObject/ServerObj/Status")
Composants = fichier.findall("FeatureObject/vServerObject/ServerObj/vComponentObject/ComponentObject")
Composants_status = fichier.findall("FeatureObject/vServerObject/ServerObj/vComponentObject/Status")

root = fichier.getroot()
feature = []
servername = []
status = []
status1 = []
composant = []

for element in root.getiterator():
    if element.tag == "FeatureName":
        print element.text
    if element.tag == "ServerName":
        print "     ",element.text,fichier.findtext("FeatureObject/vServerObject/ServerObj/Status")
    if element.tag == "ComponentName":
        print "                 :",element.text,fichier.findtext("FeatureObject/vServerObject/ServerObj/vComponentObject/ComponentObject/Status")

"""

for elem in fichier.getiterator():
    if elem.text == "SUCCESS":
        print elem.tag,elem.text
    if elem.tag == "FeatureName":
        feature = elem.text
    if elem.tag == "ServerName":
        servername = elem.text
    if elem.tag == "Status":
        status1 = elem.text
    if elem.tag == "ComponentName":
        composant =  elem.text 
    if elem.tag == "Status":
        status = elem.text
    #print ("Nom de la fonction:",feature," ","Nom du Serveur:",servername,"Etat du serveur:",status1)
"""


