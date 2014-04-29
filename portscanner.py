#!/usr/bin/python

import socket
def makeConnection(host, port):
    print "Connecting to "+host+":"+`port`
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#settimeout(value)
        s.connect((host,port))
	print "Connected"
        print s.recv(1024)
        s.close()
    except s.timeout:
        print "Time out"
    except s.error:
        print "Err"
    

makeConnection("stackoverflow.com", 80)
