GRANT ALL PRIVILEGES ON *.* TO '${DB_USER}'@'%' IDENTIFIED BY '${DB_PASSWORD}' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS userDB;

USE userDB;

DROP TABLE IF EXISTS HashChange;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS HashingAlgorithm;

CREATE TABLE HashingAlgorithm (
    id INT AUTO_INCREMENT PRIMARY KEY,
    algo VARCHAR(255) NOT NULL,
    round INT NOT NULL
);

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    hashing_algorithm INT NOT NULL,
    profile_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (hashing_algorithm) REFERENCES HashingAlgorithm(id)
);

CREATE TABLE HashChange (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    new_hashing_algorithm INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (new_hashing_algorithm) REFERENCES HashingAlgorithm(id)
);

INSERT INTO HashingAlgorithm (algo, round) VALUES ('bcrypt', 10 );
INSERT INTO HashingAlgorithm (algo, round) VALUES ('sha256', 64 );
INSERT INTO HashingAlgorithm (algo, round) VALUES ('blake2b_256', 1 );
INSERT INTO Users (username, password_hash, salt, hashing_algorithm, profile_name, email, is_admin) VALUES ('admin', '$2a$10$Jy/dPD15yoTHZrxJgQ0d6uNZ0Qe0cKJd.tnNabDRgKtEaRyKCImMu', 'u9jas8dDKs', 1, 'Administrator', 'admin@duckduck.com', TRUE);
INSERT INTO Users (username, password_hash, salt, hashing_algorithm, profile_name, email) VALUES ('user', '$2a$10$jTcXRB9kXVu1kkpKNnlHKOTVSW0dQJ3urmz4U7K21F0mrFk/5HAtG', 'o2n8aeVYDd', 1, 'User', 'user@duckduck.com');

