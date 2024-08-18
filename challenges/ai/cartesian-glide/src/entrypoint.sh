#!/bin/bash

socat TCP-LISTEN:1000,reuseaddr,fork SYSTEM:'python /usr/src/app/server.py' 2>/dev/null &

wait -n
exit $?
