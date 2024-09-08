package main

import (
	"bufio"
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"log"
	"net"
	"os"
	"regexp"
	"time"
)

func readFile(filePath string) []string {
	// Read passwords from file
	passwords := make([]string, 0)
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err.Error())
		return passwords
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		passwords = append(passwords, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err.Error())
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			fmt.Println("Error closing file:", err.Error())
		}
	}(file)
	return passwords
}

func create_rainbow_table(path string) map[string]string {
	// Read passwords from file
	passwords := readFile(path)
	// Create a hashtable to store hash -> password mappings
	rainbowTable := make(map[string]string)

	// Calculate the hash for each password and store it in the hashtable
	for _, password := range passwords {
		hash := md5_hash([]byte(password))
		rainbowTable[hash] = password
	}

	return rainbowTable
}

func md5_hash(data []byte) string {
	hasher := md5.New()
	hasher.Write(data)
	return hex.EncodeToString(hasher.Sum(nil))
}

func main() {
	rainbowTable := create_rainbow_table("rockyou.txt")

	// Connect to the TCP server
	conn, err := net.Dial("tcp", "127.0.0.1:5000")
	if err != nil {
		log.Fatal("Dial error:", err)
	}
	defer conn.Close()

	// Read messages from the TCP server
	message := make([]byte, 1024)

	_, err = conn.Read(message)
	if err != nil {
		return
	}

	_, err = conn.Write([]byte("en\n"))
	if err != nil {
		return
	}

	for {
		message = make([]byte, 1024)
		_, err := conn.Read(message)
		if err != nil {
			log.Println("Read error:", err)
			break
		}
		log.Printf("Received: %s", message)

		// Parse the received message
		re2 := regexp.MustCompile(`: (.*)\. Send`)
		parsedResponse := re2.FindStringSubmatch(string(message))

		if len(parsedResponse) > 1 {
			hash := parsedResponse[1]
			// Print the parsed response
			if rainbowTable[hash] != "" {
				// Check if the password was already cracked
				fmt.Printf("Match found: %s\n", rainbowTable[hash])
				// Send the password to the server
				conn.Write([]byte(rainbowTable[hash] + "\n"))
			} else {
				fmt.Println("No match found")
			}
		}
		time.Sleep(100 * time.Millisecond)
	}
}
