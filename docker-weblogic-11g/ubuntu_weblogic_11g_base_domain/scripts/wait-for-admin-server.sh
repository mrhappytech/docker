#!/bin/bash
# 
# This script will wait until Admin Server is available.
# There is no timeout!
#
echo "Waiting for Admin Server on $ADMIN_HOST:$ADMIN_PORT ..."
while :
do
    (echo > /dev/tcp/$ADMIN_HOST/$ADMIN_PORT) >/dev/null 2>&1
    available=$?
    if [[ $available -eq 0 ]]; then
        echo "WebLogic Admin Server is now available. Proceeding..."
        break
    fi
    sleep 1
done