#!/opt/local/bin/python -O
from socket import socket
import ssl
s = socket()
c = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED,
                    ssl_version=ssl.PROTOCOL_SSLv3, ca_certs='ca.pem')
c.connect(('10.35.68.10',8443))
# naive and incomplete check to see if cert matches host
"""
cert = c.getpeercert()
if not cert or ('commonName', u'www.google.com') not in cert['subject'][4]:
    raise Exception('Danger!')
c.write('GET / \n')
c.close()
"""
