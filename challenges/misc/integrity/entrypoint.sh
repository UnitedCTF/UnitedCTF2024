#!/bin/sh

while :; do
    socat -dd -T180 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"/app/integrity",stderr
done