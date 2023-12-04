import paramiko
import nmap
import sys
import os
def list_hosts(ips):
	hosts = []
	scan_ssh = nmap.PortScanner()
	scan_ssh_output = scan_ssh.scan(ips,port)
	for host in scan_ssh_output["scan"]:
		hosts.insert(host["addresses"]["ipv4"])
		print(host["addresses"]["ipv4"])
	n = input("select number of host to connect:")
	return hosts[n]


def ssh_access(host,user,passw):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(host, username = user, password=passw)
    sftp = client.open_sftp()
    stdin, stdout, stderr = client.exec_command('df')

    print(stdout.read().decode())
    stdout.flush()
    stdin.flush()
    stderr.flush()
    flsys = input("Which filesystem want you duplicate? ")

    stdin, stdout, stderr = client.exec_command('sudo -S dd if='+flsys+">"+flsys[5:]+".duplicated")

    stdin.write(passw+"\n")

    stdout.channel.set_combine_stderr(True)

    print(stdout.readlines())
    sftp.get("/home/osboxes/"+flsys[5:]+".duplicated","./"+host+"_"+flsys[5:]+".duplicated")
    try:
        sftp.close()
        client.close()
    except:
        pass
        
def main():
	host = list_hosts(sys.argv[0])
	user = input("introduce root username:")
	passw = input("introduce password:")
	ssh_access(host,user,passw)
	
if __name__ == "__main__":
	main()	

