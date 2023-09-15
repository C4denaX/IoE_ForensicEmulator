import pnio_dcp
from time import sleep

ip = "172.16.238.11"
dcp = pnio_dcp.DCP(ip)

mac_address = "8a:ca:58:b9:e9:51"


while True:
	try:
		name_of_station = dcp.get_name_of_station(mac_address)
		sleep(1)
	except:
		pass
