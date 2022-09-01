import time
import os
from scapy.all import sniff, PcapWriter

def main():
    print("Starting script....")
    pkts = sniff()
    my_pcap = PcapWriter('capture.pcap')
    my_pcap.write(pkts)
    my_pcap.close()


#start
main()