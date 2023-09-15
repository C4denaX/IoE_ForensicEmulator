from scapy.all import * 
from scapy.layers import *
conf.dot15d4_protocol = 'zigbee'
conf.route.resync()

def parse_pcap(pcap_path,device):
    pcap_flow = rdpcap(pcap_path)
    for pkt in pcap_flow:
        if pkt.haslayer(Dot15d4Data):
            src = hex(int(pkt[Dot15d4Data].src_addr))
            if hex(int(pkt[Dot15d4Data].src_addr)) != '0x0':  
                pkt[Dot15d4Data].src_addr = int(device,16)
                pkt["Zigbee Network Layer"].source = int(device,16)
                pkt.show2()
        if pkt.haslayer(Raw):
            continue   
        wrpcap("traffic_"+device+".pcap",pkt,append=True)

def main(arguments):
    # if len(arguments) == 3:
        parse_pcap(arguments[1],arguments[2])

if __name__ == "__main__":
    main(sys.argv)
