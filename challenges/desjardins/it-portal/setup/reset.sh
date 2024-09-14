#!/usr/bin/bash

while true; do
        rm /opt/app/challenge/db/portal.db
        /setup.d/init.db.sh
        chown challenge:challenge /opt/app/challenge/db/portal.db
        sleep 1800
done
