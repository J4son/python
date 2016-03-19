#!/usr/bin/python

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
#       Identifiants AXL => A definir dans /opt/integration/axl.passwd
# -------------------------------------------------------------------------

rep_integration = '/opt/integration/'

try:
        filin = open(rep_integration + 'axl.passwd','r')
except:
        print "Erreur lecture identifiants dans " + rep_integration + "axl.passwd"
        sys.exit(3)

lignes  = filin.readlines()
testuser = re.search('user=(.*)',lignes[0])
testpassword = re.search('password=(.*)',lignes[1])
if testuser: ccmuser = testuser.group(1)
if testpassword: ccmpwd = testpassword.group(1)
filin.close()

if ccmuser == 'user' and ccmpwd == 'pwd':
        print "Identifiants AXL incorrects dans " + rep_integration + "axl.passwd"
        sys.exit(3)

# -------------------------------------------------------------------------
#       Declaration des variables
# -------------------------------------------------------------------------

param = {}
classes = {'sqlrep' : 'Number of Replicates Created and State of Replication','sipSession':'Cisco SIP','CTIManager':'Cisco CTI Manager','location':'Cisco Locations','hw_conference_bridge':'Cisco HW Conference Bridge Device','media_streaming_app':'Cisco Media Streaming App','licence':'Etat des licences'}
state=0
for i in range(len(sys.argv)):
      testpar = re.search('--(\w*)=(.*)',sys.argv[i])
      if testpar: param[str(testpar.group(1))]=str(testpar.group(2))

# -------------------------------------------------------------------------
#       Connexion a l'equipement
# -------------------------------------------------------------------------

url_perfmon = 'https://' + param['hostname'] + ':8443/perfmonservice/services/PerfmonPort?wsdl'
try:
        Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor,faults=False,timeout=6)
except:
        print 'Connexion AXL impossible'
        sys.exit(3)


result = Perfmon_Service.service.PerfmonCollectCounterData(param['hostname'],classes[param['action']])
if result[0] != 200:
        print 'Connexion AXL impossible (Erreur ' + str(result[0])  + ')'
        sys.exit(3)


# -------------------------------------------------------------------------
#       Traitement donnees
# -------------------------------------------------------------------------

# Replication SQL 

if param['action'] == 'sqlrep':
        Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
        resultat = Perfmon_Service.service.PerfmonCollectCounterData(param['hostname'],classes[param['action']])
        replicate_state = 0
        replicate_errors = {0 : '0 (Not Started).No subscribers exist or the Database Layer Monitor service is not running and has not been running since the subscriber was installed.',1 : '1 (Started).Replication is currently being setup.',2 : '2 (Finished).Replication setup is completed and working.', 3 : '3 (Broken).Replication failed during setup and is not working.', 4: '4 - Replication is not setup correctly'}
        for j in range(len(resultat)):
                testreg = re.search(r"^\\\\[^\\]+\\[^\\]+\\Replicate_State",resultat[j].Name)
                if testreg: replicate_state = resultat[j].Value
                if replicate_state == 2:
                        print 'OK - ' + replicate_errors[replicate_state]
                        sys.exit(0)
                else:
                        print 'ERROR - ' + replicate_errors[replicate_state]
                        sys.exit(2)


#Connexion CTI
if param['action'] == 'CTIManager':
    state=0
    Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
    resultat = Perfmon_Service.service.PerfmonCollectCounterData(param['hostname'],classes[param['action']])
    if (resultat==[]):
                print "PAS DE COMPTEUR POUR CE SERVEUR: CTI Manager"
                sys.exit(0)
    for j in range(len(resultat)):
            resultat2 = resultat[j].Name.replace("\\\\" + param['hostname'] + "\\Cisco CTI Manager\\","")
            if(re.search(r"^\\\\[^\\]+\\[^\\]+\\CTIConnectionActive",resultat[j].Name)):
                    if (resultat[j].Value < 2500):
                            print "OK-",resultat2,": ",resultat[j].Value
                            state=1

    if (state == 1):
            sys.exit(0)
    else:
            sys.exit(2)



#Nombre de session SIP

if param['action'] == 'sipSession':
    if len(sys.argv) == 5:
            pass
    else:
            print "Manque les arguments seuil et valeur max"
            sys.exit(3)

    valeur_seuil = int(sys.argv[3])
    valeur_max = int(sys.argv[4])
    valeur_seuil = (valeur_seuil * valeur_max)/100
    Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
    resultat = Perfmon_Service.service.PerfmonCollectCounterData(param['hostname'],classes[param['action']])
    if (resultat==[]):
        print "PAS DE COMPTEUR POUR CE SERVEUR: sipSession"
        sys.exit(0)
    for j in range(len(resultat)):
            testreg = re.search(r"^\\\\[^\\]+\\[^\\]+\\CallsActive",resultat[j].Name)
            if testreg:
                if (resultat[j].Value < valeur_seuil):
                        resultat[j].Name = resultat[j].Name.replace("\\\\" + param['hostname'] + "\Cisco SIP(SIP_","")
                        state = 1
                        print "OK- " + resultat[j].Name.replace(")\\",":") + " => " + str(resultat[j].Value)
                else:
                        resultat[j].Name = resultat[j].Name.replace("\\\\" + param['hostname'] + "\Cisco SIP(SIP_","")
                        print "ERREUR- " + resultat[j].Name.replace(")\\",":") + " => " + str(resultat[j].Value)

    if (state == 1):
            sys.exit(0)
    else:
            sys.exit(2)

#Cisco Locations
if param['action'] == 'location':
        state=0
        Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
        resultat = Perfmon_Service.service.PerfmonCollectCounterData(param['hostname'],classes[param['action']])
        if (resultat==[]):
                print "PAS DE COMPTEUR POUR CE SERVEUR: location"
                sys.exit(0)
        BandWidthAvailable = 0
        BandWidthMaximum = 0
        for j in range(len(resultat)):
                result = resultat[j].Name.replace("\\\\" + param['hostname'] + "\\" + "Cisco Locations" ,"")
                result = result.rsplit("\\")[1]
                if (re.search(r"\\\\[^\\]+\\+[^\\]+\\BandwidthAvailable",resultat[j].Name)):
                        BandWidthAvailable = resultat[j].Value
                if (re.search(r"\\\\[^\\]+\\+[^\\]+\\BandwidthMaximum",resultat[j].Name)):
                        BandWidthMaximum = resultat[j].Value
                if ((BandWidthAvailable == 0) & (BandWidthAvailable <> BandWidthMaximum)):
                        state = 0
                        print ("ERREUR- ") + resultat[j].Name.replace("\\\\" + param['hostname'] + "\\" + "Cisco Locations","").replace("\BandwidthMaximum","") + " Available: " + str(BandWidthAvailable) + " Total: " + str(BandWidthMaximum)
                else:
                        state = 1
                        print ("OK- ") + resultat[j].Name.replace("\\\\" + param['hostname'] + "\\" + "Cisco Locations","").replace("\BandwidthMaximum","") + " Available: " + str(BandWidthAvailable) + " Total: " + str(BandWidthMaximum)
        if (state == 1):
                sys.exit(0)
        else:
                sys.exit(2)

#Cisco HW Conference Bridge
if param['action'] == 'hw_conference_bridge':
        state=0
        Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
        resultat = Perfmon_Service.service.PerfmonCollectCounterData(param['hostname'],classes[param['action']])
        ResourceAvailable = 0
        ResourceTotal = 0
        if (resultat==[]):
                print "PAS DE COMPTEUR POUR CE SERVEUR: hw_confecenre_bridge"
                sys.exit(0)
        for j in range(len(resultat)):
                result = resultat[j].Name.replace("\\\\" + param['hostname'] + "\\" + "Cisco HW Conference Bridge Device" ,"")
                result = result.rsplit("\\")[1]
        if (re.search(r"\\\\[^\\]+\\+[^\\]+\\ResourceAvailable",resultat[j].Name)):
                ResourceAvailable = resultat[j].Value
                if (re.search(r"\\\\[^\\]+\\+[^\\]+\\ResourceTotal",resultat[j].Name)):
                        ResourceTotal = resultat[j].Value
                        if ((ResourceAvailable == 0) & (ResourceAvailable <> ResourceTotal)):
                                state = 0
                                print ("ERREUR- ") + "ResourceAvailable" + ": " + str(ResourceAvailable)
                        else:
                                state = 1
                                print ("OK- ") + "ResourceAvailable" + ": " + str(ResourceAvailable)
 

        if (state == 1):
                sys.exit(0)
        else:
                sys.exit(2)


#Cisco Media Streaming App
if param['action'] == 'media_streaming_app':
        state=0
        Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
        resultat = Perfmon_Service.service.PerfmonCollectCounterData(param['hostname'],classes[param['action']])
        MTPStreamsAvailable = 0
        MTPStreamsTotal = 0
        seuil = 0
        for j in range(len(resultat)):
                result = resultat[j].Name.replace("\\\\" + param['hostname'] + "\\" + "Cisco Media Streaming App" ,"")
                result = result.rsplit("\\")[1]
                if (re.search(r"\\\\[^\\]+\\+[^\\]+\\MTPStreamsAvailable",resultat[j].Name)):
                        MTPStreamsAvailable = resultat[j].Value
                if (re.search(r"\\\\[^\\]+\\+[^\\]+\\MTPStreamsTotal",resultat[j].Name)):
                        MTPStreamsTotal = resultat[j].Value
                        seuil = 0.9 * MTPStreamsTotal
                        if (MTPStreamsAvailable < (MTPStreamsTotal - seuil)):
                                state = 0
                                print ("ERREUR- ") + "MTPStreamsAvailable" + ": " + str(MTPStreamsAvailable)
                        else:
                                state = 1
                                print ("OK- ") + "MTPStreamsAvailable" + ": " + str(MTPStreamsAvailable)


        if (state == 1):
                sys.exit(0)
        else:
                sys.exit(2)

#Etat des licences
if param['action'] == 'licence':
        state=0
        url = ("file:///opt/integration/axlsqltoolkit/schema/7.1/WSDL-AXIS/AXLAPI.wsdl")
        Perfmon_Service = suds.client.Client(url,username=ccmuser,password=ccmpwd,doctor=doctor)
        resultat = Perfmon_Service.service.executeSQLQuery("select distributedlicenseunits,usedlicenseunits from licensedistributionused where tklicensefeature = 2")
        if (resultat==[]):
                print "PAS DE COMPTEUR POUR CE SERVEUR: licence"
                sys.exit(0)
        resultat = str(resultat).replace(" ","").replace("(reply){\nreturn=\n(return){\nrow[]=\n(anyType){\n","").replace("\n},}}","").split("\n")
        Compteur_licence_utilise = resultat[1].split("=")
        Name_licence_utilise = Compteur_licence_utilise[0]
        Value_licence_utilise = int(Compteur_licence_utilise[1].replace("\"",""))
        Compteur_licence_total = resultat[0].split("=")
        Name_licence_total = Compteur_licence_total[0]
        Value_licence_total = int(Compteur_licence_total[1].replace("\"",""))

        if(Value_licence_utilise > (80 * Value_licence_total)/100):
            print "Pas assez de licences! ","Total: ",Value_licence_total,"Utilise: ",Value_licence_utilise
        else:
                print "Licences Utilisees: ",Value_licence_utilise,"Licences Totales:",Value_licence_total
                state=1
        if (state == 1):
                sys.exit(0)
        else:
                sys.exit(2)


