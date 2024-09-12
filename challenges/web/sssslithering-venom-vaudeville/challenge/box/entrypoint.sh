#!/bin/bash

./app &
sleep 1

while true; do
    echo "Start cleanup"
    sudo -u user timeout 30 ./cleanup.sh
    echo "Cleanup finished"
    sleep 60
done
