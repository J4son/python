#!/usr/bin/python -O 
import lxml,os,sys,datetime,subprocess,glob
from lxml import etree

serveur_type = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
host = sys.argv[4]

if (len(sys.argv) < 5):
        print ("Erreur pas assez de parametre !!! ")
        sys.exit(2)

rep_backup = "/opt/integration/backup_toip/"
retcode  = subprocess.call(["rm -rf ",rep_backup,"*.xml"],shell=True)
if retcode <> 0 :
	print ("erreur, impossible de supprimer le fichier",retcode)

###################RECUP DE LA DATE DU JOUR#####################################################################

date = datetime.date.today().isoformat()

###############Connexion au site distant pour recuperer le fichier xml##########################################

if (serveur_type=="CUCM"):
	subprocess.call(["cd /opt/integration/backup_toip;sftp -oPubkeyAuthentication=yes -oport=" + port + " " + user + "@" + host + ":/home/" + user + "/CallManager/" + date +"*.xml"],shell=True)
	if not glob.glob(rep_backup + date+"*.xml"):
		print ("RECUPERATION DU FICHIER IMPOSSIBLE")
		sys.exit(2)
	else:
		for myfile in  os.listdir(rep_backup):
        		if (myfile.startswith(date)):
                		document = myfile	
	
if (sys.argv[1]=="CUC"):
	subprocess.call(["cd /opt/integration/backup_toip;sftp -oPubkeyAuthentication=yes -oport=" + port + " " + user + "@" + host + ":/home/" + user + "/Unity/" + date +"*.xml"],shell=True)
	if not glob.glob(rep_backup + date+"*.xml"):
                print ("RECUPERATION DU FICHIER IMPOSSIBLE")
                sys.exit(2)
        else:
                for myfile in  os.listdir(rep_backup):
                        if (myfile.startswith(date)):
                                document = myfile
if (sys.argv[1]=="CUPS"):
	subprocess.call(["cd /opt/integration/backup_toip;sftp -oPubkeyAuthentication=yes -oport=" + port + " " + user + "@" + host + ":/home/" + user + "/CUPS/" + date +"*.xml"],shell=True)
	if not glob.glob(rep_backup + date+"*.xml"):
                print ("RECUPERATION DU FICHIER IMPOSSIBLE")
                sys.exit(2)
        else:
                for myfile in  os.listdir(rep_backup):
                        if (myfile.startswith(date)):
                                document = myfile

################renommage du fichier avec le type de server (CUPS,CUCM,...################################################################

document_origine = document
document = serveur_type + "_" + document
retcode = subprocess.call(["mv " + rep_backup + document_origine + " " + rep_backup + document],shell=True)

if retcode <> 0:
	print ("impossible de renommer le fichier")
	sys.exit(2)

############Parsing du fichier pour connaitre l etat des sauvegardes############################################

parser = lxml.etree.XMLParser()
fichier = rep_backup + document
fichier = open(fichier,"r")

if not fichier:
	print ("impossible d'ouvrir le fichier")
	sys.exit(2)

fichier_xml = lxml.etree.parse(fichier,parser)
root = fichier_xml.getroot()
servername = []
componentname = []
status = []
#resultat = lxml.etree.tostring(fichier_xml.getroot(),pretty_print=True,method="XML")

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




