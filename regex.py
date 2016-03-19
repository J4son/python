import sys,ssh
hostname = "172.16.5.130"
port = 22
username = "root"
password = "espace"
toto = ssh.SSHClient()

toto.connect(hostname,port,username,password,pkey=None, key_filename=None, timeout=None, allow_agent=True, look_for_keys=False, compress=True)
shell = toto.invoke_shell()
#print repr(shell.get_transport())

shell.exec_command("ls -lsha")

"""
import lxml,sys
from lxml import etree
servername = []
componentname = []

fichier = etree.parse("/Users/brur/Desktop/CUCM_2011-08-24-02-00-00_drfComponent.xml")
root = fichier.getroot()

for elem2 in root.iterdescendants(tag="FeatureName"):
        print elem2.tag,elem2.text
for element in root.iterdescendants(tag="ServerName"):
        print element.tag,element.text
        for elem in root.iterdescendants(tag="ComponentName"):
                print "                                       ",elem.text
for elem3 in root.iterdescendants(tag="Status"):
        print element.text,elem.text,elem3.tag,elem3.text
        
"""



"""
for element in fichier.iter(tag=etree.Element):
        if element.tag == "ServerName":
                servername.append((element.tag, element.text))
                print element.getchildren()
        elif element.tag == "Status":
                print("%s - %s" % (element.tag, element.text))
                #print element.values()
        elif element.tag == "ComponentName":
                print("%s - %s" % (element.tag, element.text))
        elif element.tag == "Status":
                print("%s - %s" % (element.tag, element.text))
"""
