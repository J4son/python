#!/usr/bin/python
import logging,suds,suds.xsd.doctor,sys,re
cache = suds.cache.ObjectCache(location="/tmp/suds",months=24)
#logging.basicConfig(level=logging.DEBUG)
doctor = suds.xsd.doctor #mise en oeuvre due l'inspection du WSDL
imp = suds.xsd.doctor.Import('http://schemas.xmlsoap.org/soap/encoding/') #ajout des URL des schemas pour interpreter le WSDL
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/soap/')
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://www.w3.org/2001/XMLSchema')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/ControlCenterServices/')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/LogCollection/')
doctor = suds.xsd.doctor.ImportDoctor(imp) #parsing du WSDL sur le serveur CCM distant
buf=""
#variable de connexion
cucm = '10.35.68.10'
ccmuser = 'brurauc'
ccmpwd = '00000'
classe = "Cisco H323"

url_perfmon = 'https://' + cucm + ':8443/perfmonservice/services/PerfmonPort?wsdl'
Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
resultat = Perfmon_Service.service.PerfmonListCounter(cucm,classe)
url_perfmon2 = 'https://' + cucm + ':8443/perfmonservice/services/PerfmonPort?wsdl'
Perfmon_Service2 = suds.client.Client(url_perfmon2,username=ccmuser,password=ccmpwd,doctor=doctor)
resultat2 = Perfmon_Service2.service.PerfmonCollectCounterData(cucm,classe)
for i in range(len(resultat2)):
        print resultat2[i].Name

"""
for j in range(len(resultat)):
        resultat[j].Name = resultat[j].Name.replace(("\\" + cucm + "\\"),"")
        resultat[j].Name = resultat[j].Name.replace(classe,"")
        resultat[j].Name = resultat[j].Name.replace("\\","")
        #if (re.search(gateway,resultat[j].Name)) and (re.search('CallsActive',resultat[j].Name)) and (re.search('S0_SU0_DS1-0',resultat[j].Name)):
        #        buf += str(resultat[j].Value)
        print resultat[j]
#sys.stdout.write('%s' % (buf))
#sys.stdout.flush()
"""



"""
url = ("https://" + cucm + ":8443/axl/")
#url=("https://" + cucm + ":8443/realtimeservice/services/RisPort?wsdl")
Perfmon_Service = suds.client.Client(url,username=ccmuser,password=ccmpwd,doctor=doctor)
#resultat = Perfmon_Service.service.executeSQLQuery("select distributedlicenseunits,usedlicenseunits from licensedistributionused where tklicensefeature = 2")
print Perfmon_Service

"""




"""
resultat = str(resultat).replace(" ","").replace("(reply){\nreturn=\n(return){\nrow[]=\n(anyType){\n","").replace("\n},}}","").split("\n")

Compteur_licence_utilise = resultat[1].split("=")
Name_licence_utilise = Compteur_licence_utilise[0]
Value_licence_utilise = int(Compteur_licence_utilise[1].replace("\"",""))

Compteur_licence_total = resultat[0].split("=")
Name_licence_total = Compteur_licence_total[0]
Value_licence_total = int(Compteur_licence_total[1].replace("\"",""))

if(Value_licence_utilise < (80 * Value_licence_total)/100):
    print "Pas assez de licences"
"""
"""
url_perfmon = 'https://' + cucm + ':8443/perfmonservice/services/PerfmonPort?wsdl'
Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
resultat = Perfmon_Service.service.PerfmonListCounter(cucm)

for j in range(len(resultat)):
	
	classe = buf = ''
	classe = str(resultat[j].Name)
	
	Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
	resultat2 = Perfmon_Service.service.PerfmonCollectCounterData(cucm,classe)

	for i in range(len(resultat2)):
        	buf += str(resultat2[i].Name) + " => " + str(resultat2[i].Value) + "\n"

	sys.stdout.write('\n-------------------------------------------------------\n')
	sys.stdout.write('  ' + classe + '\n')
	sys.stdout.write('-------------------------------------------------------\n\n')
	sys.stdout.write('%s' % (buf))


sys.stdout.flush()
"""
