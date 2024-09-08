package main

// Every 5 seconds, the victim try logins with admin and FLAG to the webserver

import (
	"log"
	"net/http"
	"os"
	"strings"
	"time"
)

func main() {
	targetIP := os.Getenv("WEBSERVER_IP")
	port := os.Getenv("PORT")
	username := "admin"
	password := os.Getenv("PASSWORD")
	targetURL := "http://" + targetIP + ":" + port + "/login"
	body := "username=" + username + "&password=" + password
	for {
		log.Println("Trying to login to the web server at " + targetURL + "...")
		if get, err := http.Post(targetURL, "application/x-www-form-urlencoded", strings.NewReader(body)); err != nil {
			log.Printf("Error: %v\n", err)
		} else {
			log.Printf("Response: %s\n", get.Status)
		}
		time.Sleep(5 * time.Second)
	}
}
