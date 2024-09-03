#!/bin/bash

echo "[mysqld]" >>/etc/mysql/my.cnf
echo "bind-address = 127.0.0.1" >>/etc/mysql/my.cnf

service mariadb start
echo -e "\nY\nY\n$DB_PASSWORD\n$DB_PASSWORD\nY\nn\nY\nY\n" | mysql_secure_installation
# Read the SQL script
sql=$(cat /db/db.sql)

# Replace the placeholders with the environment variable values
sql=${sql//\$\{DB_PASSWORD\}/$DB_PASSWORD}
sql=${sql//\$\{DB_USER\}/$DB_USER}

# Execute the SQL script
echo "$sql" | mysql -u "$DB_USER" -p"$DB_PASSWORD"
