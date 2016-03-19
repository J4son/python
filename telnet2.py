#--------------------------------------------
#CLIENT TELNET
#
#--------------------------------------------
import socket

#msg= '\nhello je suis le client\n\n'
HOST = 'localhost'
PORT = 8082
user = raw_input ("enter your user:")
passwd = raw_input ("enter your password:")
msg = user + ":" + passwd

#---------------------------------------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
sock.send(msg)
donnees = sock.recv(1024)
sock.close()

