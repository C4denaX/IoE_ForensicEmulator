#!/bin/bash
docker run -d -v /var/run/docker.sock:/var/run/docker.sock gaiaadm/pumba:master $1
