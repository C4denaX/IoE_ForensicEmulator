#!/bin/bash

# Check that exactly 3 parameters are provided
if [ "$#" -ne 3 ]; then
    echo "Error: Incorrect number of parameters."
    echo "Usage: $0 <Remote_Host_IP> <Remote_File> <Local_File>"
    echo "   Remote_Host_IP: The IP address of the remote host."
    echo "   Remote_File:    The path to the file on the remote host to be accessed."
    echo "   Local_File:     The path to the local file where the output will be stored."
    exit 1
fi

# Parameters
REMOTE_HOST_IP=$1
REMOTE_FILE=$2
LOCAL_FILE=$3

# Execute the SSH command and redirect the output
ssh $REMOTE_HOST_IP "tail -f $REMOTE_FILE" > $LOCAL_FILE
