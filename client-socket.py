
import socket
import sys
# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
host = '192.168.0.10' # server address
port = '8000'#port = int(sys.argv[2]) # server port
s.connect((host, port))

# read echo
i = 0
while(i <= 1):
    data = s.recv(1000000) # read up to 1000000 bytes
    i += 1
    if (i < 5): # look only at the first part of the message
        print data
    if not data: # if end of data, leave loop
        break
    print 'received', len(data), 'bytes'

# close the connection
s.close()
