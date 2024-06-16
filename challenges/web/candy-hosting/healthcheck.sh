#!/bin/bash
set -euo pipefail

# Remove websites after 1h
OUT_FOLDER_PREFIX="${OUT_FOLDER_PREFIX:-/var/www/html/websites}"
find "${OUT_FOLDER_PREFIX}" -maxdepth 1 -type d -cmin +60 | xargs rm -rf

HTTP_CODE=$(curl -sI -H "User-Agent: healthcheck/1.0" -o /dev/null -w "%{http_code}" localhost:80)
if [ "$HTTP_CODE" -ne 200 ]; then
  exit 1
fi

exit 0
