#! /usr/bin/env python
from scapy.all import *
ans,unans = sr(IP(dst="10.10.111.1")/TCP(dport=(0,100),flags="S"),retry=3)
unfil, fil = sr(IP(dst="10.10.111.1")/TCP(dport=(0,100),flags="A"),retry =3)
print "List of ports that are close:"
ans.nsummary(lfilter=lambda(s,r):r.sprintf("%TCP.flags%")=="RA",prn=lambda(s,r):r.sprintf("%TCP.sport% is close"))
print "\nList of ports that are open:"
ans.nsummary(lfilter=lambda(s,r):r.sprintf("%TCP.flags%")=="SA",prn=lambda(s,r):r.sprintf("%TCP.sport% is open"))
print "\nList of ports that are filtered"
if fil:
	for s in fil:
		print str(s[TCP].dport) + "is filtered"
else:
	print "None"
