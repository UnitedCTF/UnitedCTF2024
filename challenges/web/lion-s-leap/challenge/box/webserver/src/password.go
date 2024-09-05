package main

import (
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"golang.org/x/crypto/bcrypt"
	"golang.org/x/crypto/blake2b"
	"math/rand"
)

func checkPassword(password string, hash string, salt string, algo string, round int) bool {
	// Compare the password with the hash
	password = salt + password
	switch algo {
	case "bcrypt":
		err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
		if err == nil {
			return true
		}
	case "sha256":
		for i := 0; i < round; i++ {
			hashBytes := sha256.Sum256([]byte(password))
			password = hex.EncodeToString(hashBytes[:])
		}
		if password == hash {
			return true
		}
	case "blake2b_256":
		for i := 0; i < round; i++ {
			hashBytes := blake2b.Sum256([]byte(password))
			password = hex.EncodeToString(hashBytes[:])
		}
		if password == hash {
			return true
		}
	default:
		return false
	}

	return false
}

const charset = "abcdefghijklmnopqrstuvwxyz" +
	"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

func generateRandomAlphanumeric(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = charset[rand.Intn(len(charset))]
	}
	return string(b)
}

func hashPassword(password string, algo string, round int) (string, string, error) {
	var hash string
	salt := generateRandomAlphanumeric(10)
	password = salt + password
	switch algo {
	case "bcrypt":
		hashBytes, err := bcrypt.GenerateFromPassword([]byte(password), round)
		if err != nil {
			return "", "", err
		}
		hash = string(hashBytes)
	case "sha256":
		for i := 0; i < round; i++ {
			hashBytes := sha256.Sum256([]byte(password))
			password = hex.EncodeToString(hashBytes[:])
		}
		hash = password
	case "blake2b_256":
		for i := 0; i < round; i++ {
			hashBytes := blake2b.Sum256([]byte(password))
			password = hex.EncodeToString(hashBytes[:])
		}
		hash = password
	default:
		return "", "", errors.New("unsupported hashing algorithm")
	}

	return hash, salt, nil
}
