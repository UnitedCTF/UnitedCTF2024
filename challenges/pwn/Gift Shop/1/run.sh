#!/bin/sh

while :; do
    socat -dd -T1800 tcp-l:2004,reuseaddr,fork,keepalive,su=nobody exec:"python3 /app/server.py",stderr
done