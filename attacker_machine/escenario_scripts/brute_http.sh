#!/bin/bash

IP="$1"
PORT="$2"
USERNAME_LIST="$3"
PASSWORD_LIST="$4"
FORM_PATH="$5"
USERNAME_PARAM="$6"
PASSWORD_PARAM="$7"
FAILURE_MESSAGE="$8"

if [ $# -ne 8 ]; then
    echo "Usage: $0 <IP> <PORT> <username_list> <password_list> <form_path> <username_param> <password_param> <failure_message>"
    exit 1
fi

hydra -L "$USERNAME_LIST" -P "$PASSWORD_LIST" "$IP" -s "$PORT" http-post-form "$FORM_PATH:$USERNAME_PARAM=^USER^&$PASSWORD_PARAM=^PASS^&Login=Login:$FAILURE_MESSAGE"
