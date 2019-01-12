#! /usr/bin/env python
from scapy.all import *
openports=[]
for dst_port in range(0,101):
	for count in range (0,3):
		ans,unans=sr(IP(dst="10.10.111.1")/UDP(dport=dst_port),timeout=10)
		if unans:
			openports.append(unans)
			break
print "The following UDP ports are open"
UDP_REVERSE = dict((UDP_SERVICES[k],k)for k in UDP_SERVICES.keys())
for i in openports:
	port_num = i[0][UDP].dport
	if port_num in UDP_REVERSE.keys():
		print "UDP port " + str(port_num) + " running service " + str(UDP_REVERSE[port_num])
	else:
		print "UDP port " + str(port_num)
print "verifying service domain"
ans, unans=sr(IP(dst="10.10.111.1")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.google.com")))
if ans:
	print ans
