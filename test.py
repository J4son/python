import httplib, urllib
params = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
     <SOAP-ENV:Body>
         <axl:getPhone xmlns:axl="http://www.cisco.com/AXL/1.0" 
xsi:schemaLocation="http://www.cisco.com/AXL/1.0 http://ccmserver/schema/axlsoap.xsd"  
sequence="1234">
             <phoneName>SEP222222222245</phoneName>
         </axl:getPhone>
     </SOAP-ENV:Body>
 </SOAP-ENV:Envelope> """
#headers = {"Content-type": "application/x-www-form-urlencoded",
#            "Accept": "text/plain"}


headers = {"POST":"8443/axl",
           "Host":"24.129.171.9",
           "Accept":"text/*",
           "Authorization":"Basic bGFycnk6Y3VybHkgYW5kIG1vZQ==",
           "Content-type":"text/xml",
           "Content-length":"613"}

conn = httplib.HTTPConnection("24.129.171.9")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()


"""
POST :8443/axl
 Host: axl.myhost.com:80
 Accept: text/*
 Authorization: Basic bGFycnk6Y3VybHkgYW5kIG1vZQ==
 Content-type: text/xml
 Content-length: 613
 <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
     <SOAP-ENV:Body>
         <axl:getPhone xmlns:axl="http://www.cisco.com/AXL/1.0" 
xsi:schemaLocation="http://www.cisco.com/AXL/1.0 http://ccmserver/schema/axlsoap.xsd"  
sequence="1234">
             <phoneName>SEP222222222245</phoneName>
         </axl:getPhone>
     </SOAP-ENV:Body>
 </SOAP-ENV:Envelope>
"""





"""
import nmap,pygeoip
gi = pygeoip.GeoIP('/Users/brur/Desktop/GeoIP.dat', pygeoip.MEMORY_CACHE)
 
scan = nmap.PortScanner()
toto = scan.scan(hosts='127.0.0.1',ports='1-1024',arguments='-sV')



import ssh,sys,socket
from ssh import SSHClient
hostname = '172.27.0.16'
port = 22
username = 'root'
password = 'disraeli'

connect_to_host = SSHClient()
connect_to_host.load_system_host_keys()
connect_to_host.set_missing_host_key_policy(ssh.WarningPolicy)
connect_to_host.connect(hostname,username=username,password=password)
stdin, stdout, stderr = connect_to_host.exec_command("ls -lshaR")
print stdout.read()
"""
