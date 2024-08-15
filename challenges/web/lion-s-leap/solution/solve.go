package main

import (
	"bufio"
	"encoding/hex"
	"fmt"
	"golang.org/x/crypto/blake2b"
	"os"
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

func main() {
	if len(os.Args) != 4 {
		fmt.Println("Usage: solve.go <hash> <salt> <password_file>")
		os.Exit(1)
	}
	hasher, _ := blake2b.New256(nil)
	path := os.Args[3]
	passwords := readFile(path)

	salt := os.Args[2]
	hash := os.Args[1]
	for _, password := range passwords {
		hasher.Write([]byte(salt + password))
		if hex.EncodeToString(hasher.Sum(nil)) == hash {
			fmt.Println("Password found: ", password)
			break
		}
		hasher.Reset()
	}
}
