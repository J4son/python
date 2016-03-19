#!/usr/bin/python
#-----------------------------------URL DES SERVICES WSDL UTILISE PAR LE CCM--------------------
#url = 'https://10.35.68.10:8443/perfmonservice/services/PerfmonPort?wsdl'
#url = 'https://10.35.68.10:8443/controlcenterservice/services/ControlCenterServicesPort?wsdl'
#url = 'https://10.35.68.10:8443/realtimeservice/services/RisPort?wsdl'
#url = 'https://10.35.68.10:8443/logcollectionservice/services/LogCollectionPort?wsdl'
#url = 'https://10.35.68.10:8443/CDRonDemandService/services/CDRonDemand?wsdl'
#-----------------------------------------------------------------------------------------------
import logging,suds,suds.xsd.doctor,sys
cache = suds.cache.ObjectCache(location="/tmp",months=24)
logging.basicConfig(level=logging.INFO)
doctor = suds.xsd.doctor  #mise en oeuvre due l'inspection du WSDL
imp = suds.xsd.doctor.Import('http://schemas.xmlsoap.org/soap/encoding/') #ajout des URL des schemas pour interpreter le WSDL
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/soap/')
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://www.w3.org/2001/XMLSchema')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/ControlCenterServices/')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/LogCollection/')
doctor =  suds.xsd.doctor.ImportDoctor(imp)                                                     #parsing du WSDL sur le serveur CCM distant
buf=""

if(len(sys.argv) < 2):
	print "usage : [todo]"
	sys.exit(-2)
IP = sys.argv[1]
Classe = sys.argv[2]




url_perfmon = 'https://' + IP + ':8443/perfmonservice/services/PerfmonPort?wsdl'
url_controlcenter = 'https://' + IP + ':8443/controlcenterservice/services/ControlCenterServicesPort?wsdl'
url_risport = 'https://' + IP + ':8443/realtimeservice/services/RisPort?wsdl'
url_logcollection = 'https://' + IP + ':8443/logcollectionservice/services/LogCollectionPort?wsdl'
url_cdr = 'https://' + IP + ':8443/CDRonDemandService/services/CDRonDemand?wsdl'


query = suds.client.Client(url_perfmon,username='brurauc',password='00000',doctor=doctor)
tableau = query.service.PerfmonListCounter(IP)
Perfmon_Service = suds.client.Client(url_perfmon,username='brurauc',password='00000',doctor=doctor)
resultat = Perfmon_Service.service.PerfmonCollectCounterData(IP,Classe)

for j in range(len(resultat)):
    resultat[j].Name = resultat[j].Name.replace(("\\" + IP + "\\"),"")
    resultat[j].Name = resultat[j].Name.replace(Classe,"")
    resultat[j].Name = resultat[j].Name.replace("\\","")
    buf +=resultat[j].Name.replace(" ","") + ":" + str(resultat[j].Value) + " "
   

#sys.stdout.write('%s' % (buf))
#sys.stdout.flush()

                        
         


