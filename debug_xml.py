#!/usr/bin/python 
import xml,os,sys,datetime,logging
from xml.etree.ElementTree import XMLTreeBuilder
logging.basicConfig(level=logging.DEBUG)
rep_backup =  "/Users/brur/Documents/2011-05-19-03-01-25_drfComponent.xml"

###################RECUP DE LA DATE DU JOUR#####################################################################

date = datetime.date.today().isoformat()

###############Connexion au site distant pour recuperer le fichier xml##########################################
"""
if (serveur_type=="CUCM"):
        os.system("sftp -oPubkeyAuthentication=yes -oport=" + port + " " + user + "@" + host + ":/home/" + user + "/CallManager/" + date +"*.xml")
if (sys.argv[1]=="CUC"):
        os.system("sftp -oPubkeyAuthentication=yes -oport=" + port + " " + user + "@" + host + ":/home/" + user + "/Unity/" + date +"*.xml")

if (sys.argv[1]=="CUPS"):
        os.system("sftp -oPubkeyAuthentication=yes -oport=" + port + " " + user + "@" + host + ":/home/" + user + "/CUPS/" + date +"*.xml")
"""

################recup du nom du fichier a parser################################################################

for myfile in  os.listdir(rep_backup):
        if (myfile.startswith(date)):
                document = myfile


############Parsing du fichier pour connaitre l etat des sauvegardes############################################

fichier = xml.etree.ElementTree.parse(document)
print fichier
root = fichier.getroot()
feature = []
servername = []
status = []
status1 = []
composant = []
tableau = []
state = 3
for elem in fichier.getiterator():
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
        #print feature,"\n","\n\t\t",servername,status1,composant,status
        tableau += feature,servername,status1,composant,status


