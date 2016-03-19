#--------------------------------------------
#SERVEUR TELNET
#UTILISANT TCP
#--------------------------------------------
import socket,string
host = 'localhost'
port = 8082
user = ""
passwd = ""
msg = 'Bonjour je suis le serveur'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
print "Listening on port", port, "..."
connexion, adresse = sock.accept()
while 1:
	print "accepting connection"
	print "################################"
	print "##### Connected by:        #####"
	print "#####", adresse ,  "#####"
	print "################################\n\n"
	donnees = connexion.recv(1024)
	print donnees	
	if not donnees: break
	connexion.send(msg)
	
	
	