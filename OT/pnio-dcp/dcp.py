import pnio_dcp
from time import sleep
ip = "172.16.238.10"
dcp = pnio_dcp.DCP(ip)

while True:
	identified_devices = dcp.identify_all()
	sleep(1)
