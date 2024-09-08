package main

import (
	"fmt"
	"html/template"
	"io"
	"log"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
	"strings"
	"unsafe"

	"github.com/google/uuid"
)

const (
	EAX = uint8(unsafe.Sizeof(true))
)

func getLang(r *http.Request) string {
	lang, err := r.Cookie("lang")
	if err != nil || lang == nil {
		return "en"
	}

	if lang.Value == "en" || lang.Value == "fr" {
		return lang.Value
	} else {
		return "en"
	}

}

func handlerLang(w http.ResponseWriter, r *http.Request) {
	lang := r.URL.Query().Get("l")
	if lang == "en" || lang == "fr" {
		cookie, err := r.Cookie("lang")
		if err != nil || cookie == nil {
			cookie = &http.Cookie{
				Name:  "lang",
				Value: lang,
			}
		} else {
			cookie.Value = lang
		}
		http.SetCookie(w, cookie)
	}

	http.Redirect(w, r, r.Header.Get("Referer"), http.StatusSeeOther)
}

func serveTemplate(w http.ResponseWriter, r *http.Request, contentPath string, data map[string]interface{}) {
	lang := getLang(r)

	lp := filepath.Join("templates", lang+"/layout.html")
	fp := filepath.Join("templates", filepath.Clean(lang+"/"+contentPath))
	// Parse the files into a template
	tmpl, err := template.ParseFiles(lp, fp)
	if err != nil {
		return
	}

	if data == nil {
		data = map[string]interface{}{}
	}
	data["Lang"] = lang

	// Execute the "layout" template
	err = tmpl.ExecuteTemplate(w, "layout", data)

	// Check for errors when executing the template
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func handleIndex(w http.ResponseWriter, r *http.Request) {
	// Check if the request has a session cookie
	cookie, err := r.Cookie("session_id")
	if err != nil {
		if err == http.ErrNoCookie {
			// Generate a unique session ID
			sessionID := uuid.New().String()
			encodedSessionID := url.QueryEscape(sessionID)
			// Create a new cookie
			cookie = &http.Cookie{
				Name:  "session_id",
				Value: encodedSessionID,
				Path:  "/",
			}
			// Add the cookie to the response
			http.SetCookie(w, cookie)
		} else {
			return
		}
	}

	serveTemplate(w, r, "index.html", nil)
}

func handlerFlag(w http.ResponseWriter, r *http.Request) {
	ip := r.RemoteAddr
	logFile, err := os.OpenFile("log/master_logfile.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return
	}
	defer logFile.Close()
	cookie, err := r.Cookie("session_id")

	if err != nil {
		return
	}

	// Log the session ID and IP address
	session, err := url.QueryUnescape(cookie.Value)
	_, err = logFile.WriteString(fmt.Sprintf("IP: %s, Session ID: %s\n", ip, session))
	if err != nil {
		return
	}
	log.Printf("Logged IP: %s with session: %s\n", ip, session)

	serveTemplate(w, r, "flag.html", nil)
}

func handlerLog(w http.ResponseWriter, r *http.Request) {
	fp := filepath.Join("log", "master_logfile.log")

	srcFile, err := os.Open(fp)
	if err != nil {
		serveTemplate(w, r, "log.html", nil)
		return
	}
	defer srcFile.Close()

	// Read the contents of the log file
	logContents, err := io.ReadAll(srcFile)
	if err != nil {
		return
	}

	logContents = []byte(strings.ReplaceAll(string(logContents), "\n", "<br>"))

	data := map[string]interface{}{
		"Body": template.HTML(logContents), // Use template.HTML to avoid escaping
	}

	serveTemplate(w, r, "log.html", data)
}

func main() {
	fs := http.FileServer(http.Dir("./static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	http.HandleFunc("/", handleIndex)
	http.HandleFunc("/lang", handlerLang)
	http.HandleFunc("/flag", handlerFlag)
	http.HandleFunc("/log", handlerLog)

	// Ensure the log file exists
	if _, err := os.Stat("log/master_logfile.log"); os.IsNotExist(err) {
		file, err := os.Create("log/master_logfile.log")
		if err != nil {
			log.Fatalf("Failed to create log file: %v", err)
		}
		file.Close()
	}

	port := os.Getenv("PORT")
	log.Println("Server started on :" + port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
