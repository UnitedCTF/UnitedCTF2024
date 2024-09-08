#!/bin/sh

while :; do
    socat -dd -T2 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"python /app/main.py",stderr
done