#!/bin/bash

socat TCP-LISTEN:1000,reuseaddr,fork SYSTEM:'python /usr/src/app/server1.py' &
socat TCP-LISTEN:1001,reuseaddr,fork SYSTEM:'python /usr/src/app/server2.py' &

wait -n
exit $?