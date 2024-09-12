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

INSERT INTO HashingAlgorithm (algo, round) VALUES ('bcrypt', 16 );
INSERT INTO HashingAlgorithm (algo, round) VALUES ('sha256', 64 );
INSERT INTO HashingAlgorithm (algo, round) VALUES ('blake2b_256', 1 );
INSERT INTO Users (username, password_hash, salt, hashing_algorithm, profile_name, email, is_admin) VALUES ('admin', '$2a$16$yBzd6w7J/c8zdDFJy3ZoqOos0KuUK9IJkj7hO94vRRa8Z/rLnfGwe', 'c2zSdga1Mu', 1, 'Administrator', 'admin@lionsleap.com', TRUE);

