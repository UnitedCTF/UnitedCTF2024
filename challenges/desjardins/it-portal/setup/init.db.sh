#!/usr/bin/bash

cat << EOF | sqlite3 /opt/app/challenge/db/portal.db
CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE tickets (
  ticket_id INTEGER PRIMARY KEY,
  project TEXT NOT NULL,
  ticket BLOB NOT NULL
);

INSERT INTO users (username, password) VALUES ("erika", ".4<JxYN#d283FrL");
INSERT INTO users (username, password) VALUES ("brody", "bAFWsg#W;;0488i");
INSERT INTO users (username, password) VALUES ("jeanmarie", "s1]q^/G>y9f1£m.");
INSERT INTO users (username, password) VALUES ("jane", "_3vK1/&ca%5+1-");
INSERT INTO users (username, password) VALUES ("IT", "4bcff16a998d446855176ac9901a24");

EOF
