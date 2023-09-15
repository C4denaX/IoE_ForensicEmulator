#!/bin/bash
#change traffic_0xXXXX.pcap by the device id
sudo mergecap -a traffic_0x0054.pcap traffic_0xa262.pcap traffic_0xfa82.pcap -w zigbee.pcap
