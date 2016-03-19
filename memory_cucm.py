# -------------------------------------------------------------------------
#       Import des classes
# -------------------------------------------------------------------------

import logging,suds,suds.xsd.doctor,sys,re
cache = suds.cache.ObjectCache(location="/tmp/suds",months=24)
logging.basicConfig(level=logging.INFO)
doctor = suds.xsd.doctor #mise en oeuvre due l'inspection du WSDL
imp = suds.xsd.doctor.Import('http://schemas.xmlsoap.org/soap/encoding/') #ajout des URL des schemas pour interpreter le WSDL
doctor = suds.xsd.doctor.ImportDoctor(imp) #parsing du WSDL sur le serveur CCM distant

# -------------------------------------------------------------------------
#       Connexion a l'equipement
# -------------------------------------------------------------------------
host = '10.35.68.10'
ccmuser = 'brurauc'
ccmpwd = '00000'
classes = 'Memory'

url_perfmon = 'https://' + host + ':8443/perfmonservice/services/PerfmonPort?wsdl'
try:
        Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor,faults=False,timeout=6)
except:
        print 'Connexion AXL impossible'
        sys.exit(3)


result = Perfmon_Service.service.PerfmonCollectCounterData(host,classes)
if result[0] != 200:
        print 'Connexion AXL impossible (Erreur ' + str(result[0])  + ')'
        sys.exit(3)

Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
resultat = Perfmon_Service.service.PerfmonCollectCounterData(host,classes)

if (resultat==[]):
    print "PAS DE COMPTEUR POUR CE SERVEUR: location"
    sys.exit(0)

for i in range(len(resultat)):
        if re.search("% Mem Used",resultat[i].Name):
                print resultat[i].Name.replace("\\\\" + host + "\\Memory\\",""),":",resultat[i].Value
        if re.search("% Page Usage",resultat[i].Name):
                print resultat[i].Name.replace("\\\\" + host + "\\Memory\\",""),":",resultat[i].Value
        if re.search("% VM Used",resultat[i].Name):
                print resultat[i].Name.replace("\\\\" + host + "\\Memory\\",""),":",resultat[i].Value
