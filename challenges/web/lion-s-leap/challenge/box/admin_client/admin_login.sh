#!/bin/bash

# Set the username and password
username=$ADMIN_USER
password=$ADMIN_PASS

while true
do
  echo "Logging in as $username"
  curl -s "http://localhost/login" -X POST -d "username=$username&password=$password" --insecure
  sleep 30
done
