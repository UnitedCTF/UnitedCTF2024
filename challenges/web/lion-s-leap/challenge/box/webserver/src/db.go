package main

import (
	"database/sql"
	"errors"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"os"
)

func createConnection() (*sql.DB, error) {
	// Replace with your own credentials
	ip := os.Getenv("DB_HOST")
	port := os.Getenv("DB_PORT")
	password := os.Getenv("DB_PASSWORD")
	user := os.Getenv("DB_USER")

	query := fmt.Sprintf(user + ":" + password + "@tcp(" + ip + ":" + port + ")/userDB")
	db, err := sql.Open("mysql", query)
	if err != nil {
		return nil, err
	}
	err = db.Ping()
	if err != nil {
		return nil, err
	}

	return db, nil
}

func getPasswordHash(db *sql.DB, userid int) (string, string, error) {
	var passwordHash string
	var passwordSalt string

	// Prepare the SQL statement
	err := db.QueryRow("SELECT password_hash, salt FROM Users WHERE id = ?", userid).Scan(&passwordHash, &passwordSalt)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			// No rows were returned
			return "", "", fmt.Errorf("no user found with userid %d", userid)
		}
		return "", "", err
	}

	return passwordHash, passwordSalt, nil
}

func getHashingAlgorithmFromUser(db *sql.DB, userid int) (string, int, error) {
	var hashingAlgorithm string
	var round int

	// Prepare the SQL statement
	err := db.QueryRow("SELECT HashingAlgorithm.algo, HashingAlgorithm.round FROM Users INNER JOIN HashingAlgorithm ON Users.hashing_algorithm = HashingAlgorithm.id WHERE Users.id = ?", userid).Scan(&hashingAlgorithm, &round)
	if err != nil {
		if err == sql.ErrNoRows {
			// No rows were returned
			return "", 0, fmt.Errorf("no user found with username %d", userid)
		}
		return "", 0, err
	}

	return hashingAlgorithm, round, nil
}

func getHashingAlgorithm(db *sql.DB, algo string, round int) (int, error) {
	var algoId int
	// Prepare the SQL statement
	err := db.QueryRow("SELECT id FROM HashingAlgorithm WHERE algo = ? AND round = ?", algo, round).Scan(&algoId)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			// No rows were returned
			return 0, fmt.Errorf("no algo found with %s and %d rounds", algo, round)
		}
		return 0, err
	}

	return algoId, nil
}

func getAlgorithms(db *sql.DB) ([]map[string]interface{}, error) {
	rows, err := db.Query("SELECT id,algo, round FROM HashingAlgorithm")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var algorithms []map[string]interface{}
	for rows.Next() {
		var algo string
		var round int
		var id int
		err = rows.Scan(&id, &algo, &round)
		if err != nil {
			return nil, err
		}
		algorithms = append(algorithms, map[string]interface{}{"id": id, "algo": algo, "round": round})
	}

	return algorithms, nil
}

func getUserID(db *sql.DB, username string) (int, error) {
	var id int

	err := db.QueryRow("SELECT id FROM Users WHERE username = '" + username + "'").Scan(&id)
	if err != nil {
		return 0, err
	}

	return id, nil
}

func checkUser(db *sql.DB, userId int, password string) bool {

	hash, salt, err := getPasswordHash(db, userId)
	if err != nil {
		return false
	}

	algorithm, round, err := getHashingAlgorithmFromUser(db, userId)
	if err != nil {
		return false
	}

	if !checkPassword(password, hash, salt, algorithm, round) {
		return false
	}

	return true
}

func getUserInfo(db *sql.DB, userid int) (string, string, error) {
	var name string
	var email string

	err := db.QueryRow("SELECT profile_name, email FROM Users WHERE id = ?", userid).Scan(&name, &email)
	if err != nil {
		return "", "", err
	}

	return name, email, nil
}

func createUser(db *sql.DB, username string, password string, email string, name string) error {

	hash, salt, err2 := hashPassword(password, "bcrypt", 16)
	if err2 != nil {
		return err2
	}
	_, err := db.Exec("INSERT INTO Users (username, password_hash, salt, hashing_algorithm, email, profile_name) VALUES (?, ?, ?, ?, ?, ?)", username, hash, salt, 1, email, name)
	if err != nil {
		return err
	}

	return nil
}

func isAdministrator(db *sql.DB, userid int) bool {
	var admin bool
	err := db.QueryRow("SELECT is_admin FROM Users WHERE id = ?", userid).Scan(&admin)
	if err != nil {
		return false
	}
	return admin
}

func addChangeHash(db *sql.DB, userid int, algoId int) error {
	_, err := db.Exec("INSERT INTO HashChange (user_id, new_hashing_algorithm) VALUES (?, ?)", userid, algoId)
	if err != nil {
		return err
	}

	return nil
}

func setChangeHash(db *sql.DB, userid int, password string) error {
	var algoId int
	err := db.QueryRow("SELECT new_hashing_algorithm FROM HashChange WHERE user_id = ?", userid).Scan(&algoId)
	if err != nil {
		return err
	}

	var algo string
	var round int
	err = db.QueryRow("SELECT algo, round FROM HashingAlgorithm WHERE id = ?", algoId).Scan(&algo, &round)
	if err != nil {
		return err
	}

	hash, salt, err := hashPassword(password, algo, round)

	_, err = db.Exec("UPDATE Users SET password_hash = ?, salt = ?, hashing_algorithm = ? WHERE id = ?", hash, salt, algoId, userid)
	if err != nil {
		return err
	}

	_, err = db.Exec("DELETE FROM HashChange WHERE user_id = ?", userid)
	if err != nil {
		return err
	}
	return nil
}

func setPassword(db *sql.DB, userid int, password string) error {
	algo, round, err := getHashingAlgorithmFromUser(db, userid)
	if err != nil {
		return err
	}

	hash, salt, err := hashPassword(password, algo, round)
	if err != nil {
		return err
	}
	_, err = db.Exec("UPDATE Users SET password_hash = ?, salt = ? WHERE id = ?", hash, salt, userid)
	if err != nil {
		return err
	}
	return nil
}
