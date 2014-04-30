#!/usr/bin/python
import socket
def makeConnection(host, port):
    print "|    "+`currentport`+"     |",
   # print "Connecting to "+host+":"+`port`
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    conres=s.connect_ex((host,port))
    if(conres==0):
        print "Open   |"
    else:
        print "Closed |"            
    s.close()

scanHost=raw_input("Enter the hostname/IP: ")
startRange=raw_input("Enter the start of port range:")
endRange=raw_input("Enter the end of port range:")
print "=========================================="
print ":::: Scanning "+scanHost+" ::::"
print "==========================================\n|Port Number | Status |"
for currentport in range(int(startRange),int(endRange)+1):
    makeConnection(scanHost, currentport)
print "=========================================="
