package main

import (
	"bufio"
	"crypto/md5"
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"log"
	"math/big"
	"net"
	"os"
	"strconv"
)

var TEXT = map[string]map[string]string{
	"en": {
		"welcome":  "Welcome to Hash & Funambules 2! You can choose your language: en, fr\n",
		"hash":     "Here is the hash #",
		"password": ". Send me the password.\n",
		"wrong":    "Wrong password.\n",
		"success":  "Success!\n",
		"flag":     "The flag is: ",
	},
	"fr": {
		"welcome":  "Bienvue à Hash & Funambules 2! Vous pouvez choisir votre langue: en, fr\n",
		"hash":     "Voici le hash #",
		"password": ". Envoyez-moi le mot de passe.\n",
		"wrong":    "Mauvais mot de passe.\n",
		"success":  "Correct!\n",
		"flag":     "Le flag est: ",
	},
}

type Config struct {
	FLAG string `json:"FLAG"`
}

func chooseLanguage(conn net.Conn) (string, error) {
	buffer := make([]byte, 1024)

	conn.Write([]byte(TEXT["en"]["welcome"] + TEXT["fr"]["welcome"]))

	n, err := conn.Read(buffer)
	if err != nil {
		log.Println("Error reading:", err.Error())
		return "", err
	}

	switch string(buffer[:n-1]) {
	case "en":
		return "en", nil
	case "fr":
		return "fr", nil
	default:
		conn.Write([]byte("Invalid language"))
		return "", fmt.Errorf("invalid language")
	}
}

func readFile(filePath string) []string {
	// Read passwords from file
	passwords := make([]string, 0)
	file, err := os.Open(filePath)
	if err != nil {
		log.Println("Error opening file:", err.Error())
		return passwords
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		passwords = append(passwords, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Println("Error reading file:", err.Error())
	}
	defer func(file *os.File) {
		file.Close()
	}(file)
	return passwords
}

func listen(flag string) {
	listener, err := net.Listen("tcp", ":5000")
	if err != nil {
		log.Println("Error listening:", err.Error())
		return
	}
	defer listener.Close()
	log.Println("Server is listening on port 5000")

	passwords := readFile("rockyou.txt")

	log.Println("Loaded", len(passwords), "passwords")

	for {
		// Wait for a connection
		conn, err := listener.Accept()
		if err != nil {
			log.Println("Error accepting connection:", err.Error())
			return
		}

		// Handle the connection in a new goroutine
		go handleConnection(conn, flag, passwords)
	}
}

func md5_hash(data []byte) string {
	hasher := md5.New()
	hasher.Write(data)
	return hex.EncodeToString(hasher.Sum(nil))
}

func handleConnection(conn net.Conn, flag string, passwords []string) {
	defer conn.Close()
	log.Println("Accepted new connection")
	lang, err := chooseLanguage(conn)
	if err != nil {
		return
	}

	for i := 1; i <= 1000; i++ {
		// Echo back received data
		buffer := make([]byte, 1024)

		// Generate random number to select a password
		value, err := rand.Int(rand.Reader, big.NewInt(int64(len(passwords))))
		if err != nil {
			log.Println("Error generating random number:", err.Error())
			return
		}

		password := passwords[value.Int64()%int64(len(passwords))]

		hash := md5_hash([]byte(password))
		conn.Write([]byte(TEXT[lang]["hash"] + strconv.Itoa(i) + " : " + hash + TEXT[lang]["password"]))

		// Read data from the connection
		n, err := conn.Read(buffer)
		if err != nil {
			log.Println("Error reading:", err.Error())
			return
		}

		log.Println("Received: ", string(buffer[:n-1]))

		// Check if the password is correct
		if string(buffer[:n-1]) != password {
			conn.Write([]byte(TEXT[lang]["wrong"]))
			return
		} else {
			conn.Write([]byte(TEXT[lang]["success"]))
		}
	}
	conn.Write([]byte(TEXT[lang]["flag"] + flag))
	return
}

func LoadConfiguration(file string) Config {
	var config Config
	configFile, err := os.Open(file)
	defer configFile.Close()
	if err != nil {
		log.Println(err.Error())
	}
	jsonParser := json.NewDecoder(configFile)
	jsonParser.Decode(&config)
	return config
}

func main() {
	// Load config
	config := LoadConfiguration("config.json")

	// Create a TCP listener on port 5000
	listen(config.FLAG)
}
