import random
import argparse
from scapy.all import *
import nmap
import ipaddress

used_ips = []

def get_random_ip(network):
    valid_ip = False
    while not valid_ip:
        last_part = str(random.randint(1, 254))
        final_ip = f"{network}.{last_part}"
        if final_ip not in used_ips:
            used_ips.append(final_ip)
            valid_ip = True
    return final_ip

def select_type_scan(scan_type):
    scan_arguments = {
        "1": "-sS",  # TCP SYN scan
        "2": "-sT",  # TCP connect scan
        "3": "-sU",  # UDP Scan
        "4": "-sN",  # TCP NULL
        "5": "-sF",  # TCP FIN
        "6": "-sX",  # TCP XMAS
        "7": "-sA"   # TCP ACK
    }
    return scan_arguments.get(scan_type, "-sS")

def scan_network(ip, network, scan_type, port_range):
    scan = nmap.PortScanner()
    while True:
        try:
            scan_arguments = f"-p{port_range} {select_type_scan(scan_type)}"
            scan.scan(hosts=network, arguments=scan_arguments)
            print(scan.scanstats())
        except KeyboardInterrupt:
            option = input("Would you like to finish (F) or change scan type (C): ")
            if option.lower() == "c":
                scan_type = input("Enter new scan type (1-7): ")
            else:
                exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Scanner Script")
    parser.add_argument('--network', type=str, required=True, help="Network to scan (e.g., 192.168.1.0/24)")
    parser.add_argument('--scan-type', type=str, default="1", help="Type of scan (1:TCP SYN, 2:TCP Connect, 3:UDP, 4:TCP NULL, 5:TCP FIN, 6:TCP XMAS, 7:TCP ACK)")
    parser.add_argument('--port-range', type=str, default="1-10000", help="Range of ports to scan (default is 1-10000)")
    parser.add_argument('--threads', type=int, default=1, help="Number of threads for scanning (not yet implemented)")

    args = parser.parse_args()

    # Validate network
    try:
        ip_network = ipaddress.ip_network(args.network, strict=False)
    except ValueError as e:
        print(f"Invalid network address: {e}")
        exit(1)

    src_ip = get_random_ip(ip_network.network_address)

    scan_network(src_ip, args.network, args.scan_type, args.port_range)
