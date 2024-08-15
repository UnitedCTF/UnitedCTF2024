#!/bin/sh
/db/init_db.sh
/root/admin_login.sh &
/app/main
