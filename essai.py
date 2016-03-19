import socket,sys
print "L ordinateur s appelle",socket.gethostname()

host = '' # can leave this blank on the server side
port = 8000 #port = int(sys.argv[1])
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(3)
connexion,addresse = serversocket.accept()
print 'adresse du client:',addresse

# read string from client (assumed here to be so short that one call to
# recv() is enough), and make multiple copies (to show the need for the
# "while" loop on the client side)
data = connexion.recv(1000000)
data = 10000 * data # concatenate data with itself 999 times
# wait for the go-ahead signal from the keyboard (to demonstrate that
# recv() at the client will block until server sends)
z = raw_input()
# now send
connexion.send(data)
# close the connection
connexion.close()
