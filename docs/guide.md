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

## Scenario Deployment methods

### Deploy Scenario using Docker-Compose

In order to facilitate the deployment of complex scenarios or scenarios with a large number of nodes, the use of docker-compose, through the use of docker-compose.yml is recommended. The repository has an example of such a file. To launch a scenario with docker-compose, use the following command:

```bash
    cd to/directory/with/docker-compose.yml
    docker-compose up
```
### Deploy Scenario using Mininet
It is an alternative to docker-compose and is much more suitable for devices that do not have a large amount of RAM. Mininet must be installed as described in this [guide](https://mininet.org/download/). Once installed, this option allows us to script the deployment of a network as shown in the `mininet_scenario.py` file which is a template to facilitate the creation of a test scenario or to be the starting point for others that users of the emulator may want. To deploy the scenario with Mininet, use the following command:

```bash
    python mininet_scenario.py
```

## Deploying Forensic Applications to your scenarios

In order to use the forensic tools found in the forensic_scripts directory, there are two easy ways to do this:

1. **Deploying an attacker node as a forensic node.**
The attacker node called attacker_machine has the integration of the forensic tools for easy deployment and use by users. The problem with this solution is the storage of the file system data of the different affected devices in the scenario during an attack simulation and the capture of network traffic. Firstly due to the non-persistence of the Docker containers and secondly due to the saturation of the Docker container. To solve this, a Docker Volume must be used during the deployment of this node. To do this, the following commands must be entered:

 ```bash
     docker volume create forensic_data
     docker run -it -v forensic_data:/data <attacker_node_image>
 ```
In this way we can add persistence to the data collected by the forensic container.

2. **Using the Host Machine.**
Another solution is to launch directly from the machine that is launching the network both Docker and Mininet, in this way we supply this need in both types of deployments. The only thing we need to do is to know the network that has been deployed when configuring the Docker-Compose configuration file or the Mininet deployment algorithm. Following this guide, the IP that should be used by the devices would be 172.17.0.0.0 for OT devices, 172.18.0.0.0 for IoT devices and 172.19.0.0 for IT application nodes. 

In the case of network deployment using Mininet the user already knows which device is deployed on which IP. In the case of using Docker for deployment it would be interesting to use a scanning tool to find out. For this, I would recommend using nmap (or zmap in windows systems), its installation in Linux Systems is possible thanks to the following command:

 ```bash
     sudo apt install nmap
 ```
The usage of the tool is:

 ```bash
     nmap <subnet_to_scan>
 ``` 
Once we have detected where we want to apply our forensic scripts, all of them are configured to store the information in the directory from which the script is being launched.

## Cybersecurity applications

In this section we will detail the use of the tools available in the emulator for the execution of attacks and the start of different forensic processes in the same deployed devices. 

### Cyberattack scripts usage

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
### Python Scripts for Local Deployment

In addition to Docker containers, we provide Python scripts that can be deployed locally on your host machine. These scripts offer additional flexibility for customization and testing. Here's how to use them:

1. **Navigate to the Corresponding Script:** Locate the Python script for the protocol or application you want to deploy. These scripts are available in the corresponding folder.

2. **Adapt the Script:** Open the script in your preferred text editor and adapt it to your specific localhost. You may need to configure network settings, IP addresses, or other parameters to match your environment.

3. **Run the Script:** Execute the Python script on your local host using Python 3. Replace `script.py` with the actual filename of the script you're using:

    ```bash
    python3 script.py
    ```

Remember that these Python scripts are intended for the emulator use and should be adapted to your unique situation. They provide a valuable tool for fine-tuning and testing our emulator funtionality.

*Explore, Test, and Secure IoE Networks with Confidence.*

