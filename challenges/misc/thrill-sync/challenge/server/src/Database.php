<?php

class Database extends SQLite3
{
    public function __construct($filename)
    {
        $this->open($filename);
    }

    public function login($username, $password)
    {
        $stmt = $this->prepare('SELECT * FROM users WHERE username = :username');
        $stmt->bindValue(':username', $username);
        $result = $stmt->execute();
        $row = $result->fetchArray(SQLITE3_ASSOC);
        if ($row === false) {
            return false;
        }
        if ($this->verify_password($password, $row['password'])) {
            return $this->generate_token($row['id']);
        }
        return false;
    }

    public function logout($token)
    {
        $stmt = $this->prepare('DELETE FROM tokens WHERE token = :token');
        $stmt->bindValue(':token', $token);
        $stmt->execute();
    }

    private function verify_password($password, $hash)
    {
        if (hash("sha256", $password) == $hash) {
            return true;
        }
        else {
            return false;
        }
    }


    private function generate_token($user_id)
    {
        $token = hash('sha256',$user_id . time() . rand());
        $stmt = $this->prepare('INSERT INTO tokens (token, user_id) VALUES (:token, :user_id)');
        $stmt->bindValue(':token', $token);
        $stmt->bindValue(':user_id', $user_id);
        $stmt->execute();
        return $token;
    }

    public function register($username, $password, $email)
    {
        $stmt = $this->prepare('SELECT * FROM users WHERE username = :username');
        $stmt->bindValue(':username', $username);
        $result = $stmt->execute();
        $row = $result->fetchArray(SQLITE3_ASSOC);
        if ($row !== false) {
            return false;
        }
        $stmt = $this->prepare('INSERT INTO users (username, password, email) VALUES (:username, :password, :email)');
        $stmt->bindValue(':username', $username);
        $password = hash('sha256', $password);
        $stmt->bindValue(':password', $password);
        $stmt->bindValue(':email', $email);
        $stmt->execute();
        return true;
    }


    private function userIdFromToken($token)
    {
        $stmt = $this->prepare('SELECT * FROM tokens WHERE token = :token');
        $stmt->bindValue(':token', $token);
        $result = $stmt->execute();
        $row = $result->fetchArray(SQLITE3_ASSOC);
        if ($row === false) {
            return false;
        }
        return $row['user_id'];
    }

    public function validateToken ($token)
    {
        $stmt = $this->prepare('SELECT * FROM tokens WHERE token = :token');
        $stmt->bindValue(':token', $token);
        $result = $stmt->execute();
        $row = $result->fetchArray(SQLITE3_ASSOC);
        if ($row === false) {
            return false;
        }
        return true;
    }

    public function getFlags($token)
    {
        if (!$this->validateToken($token)) {
            return false;
        }
        $user_id = $this->userIdFromToken($token);
        if ($user_id === false) {
            return false;
        }
        $stmt = $this->prepare('SELECT * FROM flags where user_id = :user_id');
        $stmt->bindValue(':user_id', $user_id);
        $result = $stmt->execute();
        $flags = [];
        while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
            $flags[] = $row['flag'];
        }
        return $flags;
    }

    public function getAttractions()
    {
        $stmt = $this->prepare('SELECT * FROM attractions');
        $result = $stmt->execute();
        $attractions = [];
        while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
            $attractions[] = $row['name'];
        }
        return $attractions;
    }

    public function getAttraction($attraction)
    {
        $stmt = $this->prepare('SELECT * FROM attractions WHERE name = :attraction');
        $stmt->bindValue(':attraction', $attraction);
        $result = $stmt->execute();
        $row = $result->fetchArray(SQLITE3_ASSOC);
        if ($row === false) {
            return false;
        }
        unset($row['id']);
        return $row;
    }
}
