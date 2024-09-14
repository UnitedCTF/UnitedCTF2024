#!/usr/bin/bash

export DEBIAN_FRONTEND=noninteractive

set -xe

FLAG="flag-813aad04a59b715ffcd9abc1d76f3c"

# install dependencies
apt update
apt install -y openssh-server ifupdown \
  sqlite3 python3 python3-paramiko curl ncat

rm -rf /usr/share/man/*
rm -rf /usr/share/doc/*
apt -y autoremove
apt clean
rm -rf /var/lib/apt/lists/*

useradd -s /usr/bin/bash -u 1001 -md /opt/app/challenge challenge
passwd -l challenge

# Create Portal Service
cat << EOF > /etc/systemd/system/portal.service
[Unit]

[Service]
RestartSec=2s
Type=simple
User=challenge
Group=challenge
WorkingDirectory=/opt/app/challenge
ExecStart=/usr/bin/python3 /opt/app/challenge/portal.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Create Service
cat << EOF > /etc/systemd/system/reset.service
[Unit]

[Service]
RestartSec=2s
Type=simple
User=reset
Group=reset
ExecStart=/setup.d/reset.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# setup flag
echo "${FLAG}" > "/$FLAG"
chmod 444 "/$FLAG"

# Setup permissions
chmod 700 /setup.d
chmod +x /setup.d/init.db.sh
chmod 750 /opt/app/challenge
chmod 750 /opt/app/challenge/keys
chmod 740 /opt/app/challenge/keys/portal.key

# Initiating DB
mkdir /opt/app/challenge/db
/setup.d/init.db.sh
chmod -R 770 /opt/app/challenge/db
chown -R root:challenge /opt/app/challenge

# Start service
systemctl daemon-reload
systemctl enable --now portal
systemctl enable --now reset

