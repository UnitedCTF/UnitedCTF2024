package main

import (
	"bufio"
	"crypto/md5"
	"crypto/rand"
	"crypto/sha1"
	"crypto/sha256"
	"crypto/sha512"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"golang.org/x/crypto/bcrypt"
	"golang.org/x/crypto/blake2b"
	"golang.org/x/crypto/sha3"
	"hash"
	"log"
	"math/big"
	"net"
	"os"
	"strconv"
)

var TEXT = map[string]map[string]string{
	"en": {
		"welcome":  "Welcome to Hash & Funambules 4! You can choose your language: en, fr\n",
		"hash":     "Here is the hash #",
		"password": ". Send me the password.\n",
		"wrong":    "Wrong password.\n",
		"success":  "Success!\n",
		"flag":     "The flag is: ",
	},
	"fr": {
		"welcome":  "Bienvue à Hash & Funambules 4! Vous pouvez choisir votre langue: en, fr\n",
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

func chooseAlgorithm() string {
	algorithms := []string{"md5", "sha1", "sha256", "sha512", "sha3", "blake2b", "bcrypt"}
	n, err := rand.Int(rand.Reader, big.NewInt(int64(len(algorithms))))
	if err != nil {
		log.Println("Error generating random number:", err)
		return ""
	}
	return algorithms[n.Int64()]
}

func hashPassword(password string, algorithm string) string {
	var hasher hash.Hash
	switch algorithm {
	case "md5":
		hasher = md5.New()
	case "sha1":
		hasher = sha1.New()
	case "sha256":
		hasher = sha256.New()
	case "sha512":
		hasher = sha512.New()
	case "sha3":
		hasher = sha3.New256()
	case "blake2b":
		hasher, _ = blake2b.New256([]byte("d6624d407ab80896d1f442b9a079b7ae"))
	case "bcrypt":
		fromPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
		if err != nil {
			return ""
		}
		return string(fromPassword)
	default:
		return ""
	}
	hasher.Write([]byte(password))
	return hex.EncodeToString(hasher.Sum(nil))
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
		err := file.Close()
		if err != nil {
			log.Println("Error closing file:", err.Error())
		}
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

	// Read the number of passwords from the file
	passwords := readFile("rockyou.txt")

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

func handleConnection(conn net.Conn, flag string, passwords []string) {
	defer conn.Close()
	log.Println("Accepted new connection")

	lang, err := chooseLanguage(conn)
	if err != nil {
		log.Println("Error choosing language:", err.Error())
		return
	}

	// Generate random number to select a password
	value, err := rand.Int(rand.Reader, big.NewInt(int64(len(passwords))))
	if err != nil {
		log.Println("Error generating random number:", err.Error())
		return
	}

	v64 := value.Int64()

	for i := 1; i <= 1000; i++ {
		// Echo back received data
		buffer := make([]byte, 4096)

		values := make([]byte, 8)
		_, err := rand.Read(values)
		if err != nil {
			log.Println("Error generating random number:", err.Error())
			return
		}
		v := values[0] ^ values[1]<<8 ^ values[2]<<16 ^ values[3]<<24 ^ values[4]<<32 ^ values[5]<<40 ^ values[6]<<48 ^ values[7]<<56
		password := passwords[v64]
		log.Println("Selected password: ", password)

		algo := chooseAlgorithm()
		hash := hashPassword(password, algo)
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
		v64 = (v64 + int64(v)) % int64(len(passwords))
	}
	conn.Write([]byte(TEXT[lang]["flag"] + flag))
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
