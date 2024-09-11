package main

// Every 5 seconds, the victim try logins with admin and FLAG to the webserver

import (
	"io"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
	"regexp"
	"sync"
	"time"
)

func main() {
	baseURL := os.Getenv("WEBSERVER_URL")

	login_form := url.Values{
		"username": {os.Getenv("USERNAME")},
		"password": {os.Getenv("PASSWORD")},
	}

	var wg sync.WaitGroup
	for {
		wg.Add(1)
		go func() {
			defer wg.Done()

			jar, err := cookiejar.New(nil)
			if err != nil {
				log.Println(err)
				return
			}

			client := &http.Client{
				Jar: jar,
			}

			log.Println("Fetching flag ...")
			resp, err := client.PostForm(baseURL+"/login", login_form)
			if err != nil {
				log.Println(err)
				return
			}
			defer resp.Body.Close()

			if resp.StatusCode != http.StatusOK {
				log.Println("Invalid status code")
				log.Println(resp.StatusCode)
				return
			}

			resp_body, err := io.ReadAll(resp.Body)
			if err != nil {
				log.Println(err)
				return
			}

			r, _ := regexp.Compile("flag: (flag-.+?)</")
			matches := r.FindStringSubmatch(string(resp_body))
			if len(matches) != 2 {
				log.Println("Unable to find flag in response")
				return
			}

			log.Println("Received flag: " + matches[1])
		}()
		wg.Wait()
		time.Sleep(5 * time.Second)
	}
}
