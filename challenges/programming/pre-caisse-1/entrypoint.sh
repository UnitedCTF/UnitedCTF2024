#!/bin/sh

while :; do
    socat -dd -T10 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"python /app/main.py",stderr
done