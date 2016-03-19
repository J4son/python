# -------------------------------------------------------------------------
#       Import des classes
# -------------------------------------------------------------------------
import logging,suds,suds.xsd.doctor,sys,re
cache = suds.cache.ObjectCache(location="/tmp/suds",months=24)
logging.basicConfig(level=logging.INFO)
doctor = suds.xsd.doctor                                                                                                #mise en oeuvre due l'inspection du WSDL
imp = suds.xsd.doctor.Import('http://schemas.xmlsoap.org/soap/encoding/')           #ajout des URL des schemas pour interpreter le WSDL
doctor = suds.xsd.doctor.ImportDoctor(imp)                                                              #parsing du WSDL sur le serveur CCM distant

# -------------------------------------------------------------------------
#       Identifiants AXL => A definir dans /opt/integration/axl.passwd
# -------------------------------------------------------------------------
ccmuser = "brurauc"
ccmpwd = "00000"
hostname = "10.35.68.10"


# -------------------------------------------------------------------------
#       Declaration des variables
# -------------------------------------------------------------------------

param = {}
classes = {'sqlrep' : 'Number of Replicates Created and State of Replication','sipSession':'Cisco SIP','CTIManager':'Cisco CTI Manager','location':'Cisco Locations','hw_conference_bridge':'Cisco HW Conference Bridge Device','media_streaming_app':'Cisco Media Streaming App','licence':'Etat des licences','registeredphone':'RegisteredHardwarePhones'}
state=0
for i in range(len(sys.argv)):
      testpar = re.search('--(\w*)=(.*)',sys.argv[i])
      if testpar: param[str(testpar.group(1))]=str(testpar.group(2))

# -------------------------------------------------------------------------
#       Connexion a l'equipement
# -------------------------------------------------------------------------

url_perfmon = 'https://' + hostname + ':8443/perfmonservice/services/PerfmonPort?wsdl'
try:
        Perfmon_Service = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor,faults=False,timeout=6)
except:
        print 'Connexion AXL impossible'
        sys.exit(3)


result = Perfmon_Service.service.PerfmonCollectCounterData(hostname,"Cisco CallManager")
if result[0] != 200:
        print 'Connexion AXL impossible (Erreur ' + str(result[0])  + ')'
        sys.exit(3)

resultat = result[1]
# -------------------------------------------------------------------------
#       Traitement donnees
# -------------------------------------------------------------------------
for j in range(len(resultat)):
    testreg = re.search(r"^\\\\[^\\]+\\[^\\]+\\RegisteredHardwarePhones",resultat[j].Name)
    if testreg:
          print resultat[j].Name.split('\\')[2] + "-" + resultat[j].Name.split('\\')[4] +": " + str(resultat[j].Value)
  
   

