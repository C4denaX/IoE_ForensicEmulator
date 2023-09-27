# Forensic (Industrial) Internet of Things Emulator - Installation Guide

Welcome to the installation guide for the Forensic (Industrial) Internet of Things Emulator. This guide will walk you through the necessary steps to set up and use our powerful emulator.

## Page Explanation

This guide provides detailed instructions for setting up the Forensic (Industrial) Internet of Things Emulator on your Linux host. Please follow the steps carefully to ensure a smooth installation process.

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

### Python Scripts for Local Deployment

In addition to Docker containers, we provide Python scripts that can be deployed locally on your host machine. These scripts offer additional flexibility for customization and testing. Here's how to use them:

1. **Navigate to the Corresponding Script:** Locate the Python script for the protocol or application you want to deploy. These scripts are available in the corresponding folder.

2. **Adapt the Script:** Open the script in your preferred text editor and adapt it to your specific localhost. You may need to configure network settings, IP addresses, or other parameters to match your environment.

3. **Run the Script:** Execute the Python script on your local host using Python 3. Replace `script.py` with the actual filename of the script you're using:

    ```bash
    python3 script.py
    ```

Remember that these Python scripts are intended for the emulator use and should be adapted to your unique situation. They provide a valuable tool for fine-tuning and testing our emulator funtionality.


---

*Explore, Test, and Secure IIoT Networks with Confidence.*

