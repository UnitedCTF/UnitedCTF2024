#!/bin/bash

while true; do php -r "include 'jobs.php'; include 'rides.php'; update_ride_times(); process_jobs();" && sleep 15; done &
apache2-foreground &

wait -n
exit $?