#!/bin/bash

master_logfile="/app/log/master_logfile.log"
warning_log_file="/app/log/warning_logfile.log"
filter="/app/filter.awk"

handle_error() {
    echo "An error occurred: $1"
}

if [ -f "$master_logfile" ]; then
    echo "Log file exists."
    grep -o "Log file:.*" $master_logfile | cut -d ':' -f 2 | while read -r file_path; do
        {
            echo "Processing log file: $file_path"
            gawk -f $filter $file_path >>$warning_log_file &
        } || handle_error "Failed to process log file: $file_path"
    done
    echo "" >$master_logfile
else
    echo "Log file does not exist."
fi
