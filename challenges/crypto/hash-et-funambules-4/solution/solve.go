package main

import (
	"bufio"
	"crypto/md5"
	"crypto/sha1"
	"crypto/sha256"
	"crypto/sha512"
	"encoding/hex"
	"fmt"
	"golang.org/x/crypto/bcrypt"
	"golang.org/x/crypto/blake2b"
	"golang.org/x/crypto/sha3"
	"hash"
	"log"
	"net"
	"os"
	"os/exec"
	"regexp"
	"time"
)

func checkHashPassword(hashed_pasword string, password string, algorithm string) bool {
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
		return bcrypt.CompareHashAndPassword([]byte(hashed_pasword), []byte(password)) == nil
	default:
		return false
	}
	hasher.Write([]byte(password))
	return hex.EncodeToString(hasher.Sum(nil)) == hashed_pasword
}

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

func parse_message(message []byte) string {
	re := regexp.MustCompile(`: (.*)\. Send me the password.`)
	parsedResponse := re.FindStringSubmatch(string(message))
	if len(parsedResponse) > 1 {
		return parsedResponse[1]
	}
	return ""
}

func idHash(hash string) []string {
	if len(hash) == 32 {
		return []string{"md5"}
	} else if len(hash) == 40 {
		return []string{"sha1"}
	} else if len(hash) == 60 {
		return []string{"bcrypt"}
	} else if len(hash) == 64 {
		return []string{"sha256", "sha3", "blake2b"}
	} else if len(hash) == 128 {
		return []string{"sha512"}
	}
	return []string{}
}

func hashcat(hash string, password_path string, algorithm string) string {

	switch algorithm {
	case "md5":
		algorithm = "0"
	case "sha1":
		algorithm = "100"
	case "sha256":
		algorithm = "1400"
	case "sha512":
		algorithm = "1700"
	case "sha3":
		algorithm = "5000"
	case "blake2b":
		algorithm = "400"
	case "bcrypt":
		algorithm = "3200"
	}
	// ... (algorithm switch case code is the same)

	tempFile, err := os.CreateTemp("", "hash")
	if err != nil {
		log.Fatal(err)
	}
	os.WriteFile(tempFile.Name(), []byte(hash), 0644)

	cmd := exec.Command("hashcat", "-a", "0", "-m", algorithm, tempFile.Name(), password_path)
	err = cmd.Start()
	if err != nil {
		log.Fatal(err)
	}

	err = cmd.Wait()
	if err != nil {
		log.Fatal(err)
	}

	output, _ := cmd.CombinedOutput()
	compile, err := regexp.Compile(hash + `:(.*)`)
	if err != nil {
		return ""
	}
	match := compile.FindStringSubmatch(string(output))
	if len(match) > 1 {
		return match[1]
	}
	return ""
}

func brute_force(hash string, passwords []string, currentPosition int, stopPosition int, algorithm string) (string, int) {
	position := currentPosition
	for _, password := range passwords[currentPosition:] {
		if checkHashPassword(hash, password, algorithm) {
			return password, position
		}
		position++
		if position == stopPosition {
			return "", 0
		}
	}
	position = 0
	for _, password := range passwords[:currentPosition] {
		if checkHashPassword(hash, password, algorithm) {
			return password, position
		}
		position++
		if position == stopPosition {
			return "", 0
		}
	}
	return "", 0
}

func main() {

	// Connect to the TCP server
	conn, err := net.Dial("tcp", "127.0.0.1:5000")
	if err != nil {
		log.Fatal("Dial error:", err)
	}
	defer conn.Close()
	message := make([]byte, 4096)
	_, err = conn.Read(message)
	if err != nil {
		return
	}

	_, err = conn.Write([]byte("en\n"))
	if err != nil {
		return
	}

	passwords := readFile("rockyou.txt")

	// Read messages from the TCP server
	position := 0
	end := 0
	flag := true
	for {
		message = make([]byte, 4096)

		_, err := conn.Read(message)
		if err != nil {
			log.Println("Read error:", err)
			break
		}
		log.Printf("Received: %s", message)

		receivedHash := parse_message(message)

		//fmt.Println("Received hash: ", receivedHash)
		password := ""
		if !flag {
			end = (position + 257) % len(passwords)
		}
		flag = false
		if len(receivedHash) > 1 {
			// Print the parsed response
			algos := idHash(receivedHash)
			for _, algo := range algos {
				//println("Algo: ", algo, " Hash: ", receivedHash, " Passwords: ", len(passwords), " Position: ", position, " End: ", end)
				p := 0
				password, p = brute_force(receivedHash, passwords, position, end, algo)
				if password != "" {
					position = p
					break
				}
			}
			println("Password: ", password, " Position: ", position)
			conn.Write([]byte(password + "\n"))
		}
		time.Sleep(1000 * time.Millisecond)
	}
}
