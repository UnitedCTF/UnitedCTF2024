#!/bin/bash

socat TCP-LISTEN:1000,reuseaddr,fork SYSTEM:'python /usr/src/app/server.py',stderr &

wait -n
exit $?
