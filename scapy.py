import socket,sys
mySock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mySock.connect(("http://www.secu-info.net",80))    
except socket.error,msg:
    print "erreur:",msg
data = "GET / HTTP/1.0 Hostname www.secu-info.net /r"
mySock.sendall(data)

mySock.close()
print "Data send:",data
print socket.gethostbyname_ex('www.google.com')

