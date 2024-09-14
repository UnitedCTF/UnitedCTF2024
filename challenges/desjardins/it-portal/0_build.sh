#!/usr/bin/bash

set -e 

NAME="it-portal"
BUILDER_NAME="${NAME}-$(openssl rand -hex 5)"

# Cleanup if something fails, you can disable if you want to troubleshoot.
cleanup() {
  incus delete -f "${BUILDER_NAME}"
  exit 1
}
trap cleanup ERR HUP INT TERM EXIT

# Launch instance and add profile
incus launch -p "${PROFILE}" images:debian/12/cloud "${BUILDER_NAME}"

# Push files (like Dockerfile's copy)
incus file push -rp ./keys "${BUILDER_NAME}/opt/app/challenge"
incus exec "${BUILDER_NAME}" -- chown -R root:root /opt/app/challenge/keys/
incus file push --uid 0 --gid 0 ./src/portal.py "${BUILDER_NAME}/opt/app/challenge/portal.py"
incus file push --uid 0 --gid 0 -p ./setup/init.db.sh "${BUILDER_NAME}/setup.d/init.db.sh"
incus file push --uid 0 --gid 0 -p ./setup/reset.sh "${BUILDER_NAME}/setup.d/reset.sh"
incus file push --uid 0 --gid 0 -p ./setup/interfaces "${BUILDER_NAME}/etc/network/interfaces"

# Restart instance so interfaces are properly brought up
incus restart "${BUILDER_NAME}"

# Launch setup script
incus exec "${BUILDER_NAME}" -- bash < 1_setup.sh

# Stop instance and export into tar.gz
incus stop "${BUILDER_NAME}"

if [[ ! -d ./out ]]; then
  mkdir ./out
fi
incus export "${BUILDER_NAME}" "./out/${NAME}.tar.gz"