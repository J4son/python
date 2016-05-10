# coding=utf-8
import socket
import string

#some user data, change as per your taste
SERVER = 'irc.root-me.org'
PORT = 6667
NICKNAME = 'daytona6753'
CHANNEL = '#root-me_challenge'

#open a socket to handle the connection
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection with the server
def irc_conn():
    IRC.connect((SERVER, PORT))

#simple function to send data through the socket
def send_data(command):
    IRC.send(command + '\n')

#join the channel
def join(channel):
    send_data("/JOIN %s" % channel)

#send login data (customizable)
def login(nickname, username=NICKNAME, password = None, realname=NICKNAME, hostname=SERVER, servername=SERVER):
    send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
    send_data("NICK " + nickname)

irc_conn()
login(NICKNAME)
join(CHANNEL)

while (1):
    buffer = IRC.recv(1024)
    msg = string.split(buffer)
    print(buffer)
    if msg[0] == "PING": #check if server have sent ping command
        send_data("PONG %s" % msg[1]) #answer with pong as per RFC 1459
    if msg[1] == 'PRIVMSG' and msg[2] == NICKNAME:
        nick_name = msg[0][:string.find(msg[0],"!")] #if a private message is sent to you catch it
        message = ' '.join(msg[3:])
        #filetxt = open('/tmp/msg.txt', 'a+') #open an arbitrary file to store the messages
        #filetxt.write(string.lstrip(nick_name, ':') + ' -> ' + string.lstrip(message, ':') + '\n') #write to the file
        #filetxt.flush() #don't wait for next message, write it now!
        send_data("privmsg candy !ep1")

        print("longueur du message: ",len(msg))
        question = msg[3]
        print(question)
        #resultat = int(question[1]) + int(question[6])
        #print(resultat)
        #send_data("privmsg candy !ep1 -rep %d" % resultat)
        print(msg)