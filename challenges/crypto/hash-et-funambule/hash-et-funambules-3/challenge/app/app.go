package main

import (
	"crypto/md5"
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"os"
	"strconv"
)

var TEXT = map[string]map[string]string{
	"en": {
		"welcome":  "Welcome to Hash & Funambules 3! You can choose your language: en, fr\n",
		"hash":     "Here is the hash #",
		"password": ". Send me the password.\n",
		"wrong":    "Wrong password.\n",
		"success":  "Success!\n",
		"flag":     "The flag is: ",
	},
	"fr": {
		"welcome":  "Bienvue à Hash & Funambules 3! Vous pouvez choisir votre langue: en, fr\n",
		"hash":     "Voici le hash #",
		"password": ". Envoyez-moi le mot de passe.\n",
		"wrong":    "Mauvais mot de passe.\n",
		"success":  "Correct!\n",
		"flag":     "Le flag est: ",
	},
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

type Config struct {
	FLAG string `json:"FLAG"`
}

func listen(flag string) {
	listener, err := net.Listen("tcp", ":5000")
	if err != nil {
		log.Println("Error listening:", err.Error())
		return
	}
	defer listener.Close()
	log.Println("Server is listening on port 5000")

	// Read the number of passwords from the file

	for {
		// Wait for a connection
		conn, err := listener.Accept()
		if err != nil {
			log.Println("Error accepting connection:", err.Error())
			return
		}

		// Handle the connection in a new goroutine
		go handleConnection(conn, flag)
	}
}

func saltedMd5Hash(data []byte, salt []byte) string {
	hasher := md5.New()
	hasher.Write(salt)
	hasher.Write(data)
	return hex.EncodeToString(hasher.Sum(nil))
}

func generateSalt() []byte {
	bytes := make([]byte, 5) // 5 bytes * 2 hex characters/byte = 10 hex characters
	_, err := rand.Read(bytes)
	if err != nil {
		log.Println("Error generating random bytes:", err)
		return nil
	}
	return []byte(hex.EncodeToString(bytes))
}
func handleConnection(conn net.Conn, flag string) {
	defer conn.Close()
	log.Println("Accepted new connection")
  fileReader, err := NewFileReader("rockyou.txt")
  if err != nil {
    return
  }

	lang, err := chooseLanguage(conn)
	if err != nil {
		log.Println("Error choosing language:", err.Error())
		return
	}

	// Generate random number to select a password
	// Generate a random salt
	salt := generateSalt()
	log.Println("Generated salt: ", string(salt))
	for i := 1; i <= 1000; i++ {
		// Echo back received data
		buffer := make([]byte, 1024)

    password, err := fileReader.RandomLine()
    if err != nil {
      log.Println("Error generating random number:", err.Error())
      return
    }

		hash := saltedMd5Hash([]byte(password), salt)

		conn.Write([]byte(TEXT[lang]["hash"] + strconv.Itoa(i) + " : " + string(salt) + ":" + hash + TEXT[lang]["password"]))

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
