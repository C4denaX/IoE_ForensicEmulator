#!/bin/bash
if [ "$#" -eq 3 ]&& ["$EUID" -eq 0]; then
  
	tcpdump -i $1 > $2

	tshark -N n -r $2 -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -E header=y -E separator=/t > $3
fi
