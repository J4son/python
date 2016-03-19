import ssh,socket,logging,email,smtplib
from email.mime.text import MIMEText
logging.basicConfig()
hostname = '172.27.0.16'
username ='root'
password= 'disraeli'
port = 22
buff = ''

client  = ssh.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(ssh.AutoAddPolicy())
client.connect(hostname,port,username=username,password=password,pkey=None,key_filename=None,timeout=None,allow_agent=True,look_for_keys=True,compress=True)
chan = client.invoke_shell(term='vt100', width=80, height=24)

chan.send('ssh root@172.27.108.1 \n')
while not buff.endswith('\'s password: '):
    resp = chan.recv(9999)
    buff += resp
else:
    chan.send("disraeli\n")

while not buff.endswith('# '):
    resp = chan.recv(9999)
    buff += resp
    
chan.send('ssh Administrator@116.134.1.10\n')
while not buff.endswith('\'s password: '):
    resp = chan.recv(9999)
    buff += resp
else:
    chan.send("Tel1dus!\n")

while not buff.endswith('admin:'):
    resp = chan.recv(9999)
    buff += resp
else:
    chan.send("\n\n\n set cli pagination off\r\n")
    resp = chan.recv(9999)
    buff += resp
    chan.send('\n\n\n show hardware\n')
    while not buff.endswith('admin:'):
        resp = chan.recv(9999)
        buff += resp

print buff   
"""
if buff.startswith(""):
    print ("Ca marche")
# Create a text/plain message
msg = MIMEText(buff)
# me == the sender's email address
# you == the recipient's email address
#msg['Subject'] = 'The contents of %s' % msg
msg['Subject'] = "Reporting RAID CUCM"
msg['From'] = "bruno.riguet@telindus.fr"
msg['To'] = "bruno.riguet@telindus.fr"
#msg['To'] = "FR_SAMS_ROC_IPCOM@telindus.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('10.35.66.9')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
"""

