#!/usr/bin/python
import socket
def makeConnection(host, port):
    #host=socket.gethostbyname(hostname)
    print "Connecting to "+host+":"+`port`
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    conres=s.connect_ex((host,port))
    if(conres==0):
        print "Port "+`port`+" is open"
    else:
        print "Port "+`port`+" is closed"            
    s.close()

for currentport in range(79,81):
    makeConnection("localhost", currentport)
makeConnection("stackoverflow.com",443 )
