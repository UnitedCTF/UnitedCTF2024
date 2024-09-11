package main

import (
	"encoding/base64"
	"html/template"
	"log"
	"net/http"
	"os"
	"path/filepath"

	"github.com/gorilla/sessions"
)

func getLang(store *sessions.CookieStore, r *http.Request) string {
	session, err := store.Get(r, "session-name")
	if err != nil || session == nil {
		return "en"
	}

	lang := session.Values["lang"]
	if lang == nil {
		return "en"
	}

	return session.Values["lang"].(string)
}

func isLogged(store *sessions.CookieStore, r *http.Request) bool {
	session, err := store.Get(r, "session-name")
	if err != nil || session == nil {
		return false
	}

	isLoggedBool := session.Values["isLogged"]
	if isLoggedBool == nil {
		return false
	}

	return session.Values["isLogged"].(bool)
}

func SetLogged(store *sessions.CookieStore, w http.ResponseWriter, r *http.Request, isLogged bool) {
	session, err := store.Get(r, "session-name")
	if err != nil {
		return
	}

	session.Values["isLogged"] = isLogged
	err = sessions.Save(r, w)
	if err != nil {
		return
	}
}

func handlerLogin(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) {
	if r.Method == "POST" {
		username := r.PostFormValue("username")
		password := r.PostFormValue("password")

		log.Println("Received login request with username: " + username + " and password: " + password)
		if username == "admin" && password == "BW0mM85LgQhY2VcjDakO@l^HU" {
			SetLogged(store, w, r, true)
			http.Redirect(w, r, "/flag", http.StatusSeeOther)
		} else {
			http.Redirect(w, r, "/login?invalidCredentials", http.StatusSeeOther)
		}
	} else {
		serveTemplate(w, r, store, "login.html", nil)
	}
}

func handlerIndex(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) {
	serveTemplate(w, r, store, "index.html", nil)
}

func handlerFlag(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) {
	serveTemplate(w, r, store, "flag.html", nil)
}

func handlerLang(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) {
	lang := r.URL.Query().Get("l")
	if lang == "en" || lang == "fr" {
		session, err := store.Get(r, "session-name")
		if err != nil {
			return
		}

		session.Values["lang"] = lang
		err = sessions.Save(r, w)
		if err != nil {
			return
		}
	}

	http.Redirect(w, r, r.Header.Get("Referer"), http.StatusSeeOther)
}

func serveTemplate(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore, contentPath string, data map[string]interface{}) {
	lang := getLang(store, r)

	lp := filepath.Join("templates", lang+"/layout.html")
	fp := filepath.Join("templates", filepath.Clean(lang+"/"+contentPath))

	// Parse the files into a template
	tmpl, err := template.ParseFiles(lp, fp)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if data == nil {
		data = map[string]interface{}{}
	}

	data["IsLogged"] = isLogged(store, r)
	data["Lang"] = lang

	// Execute the "layout" template
	err = tmpl.ExecuteTemplate(w, "layout", data)

	// Check for errors when executing the template
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func main() {
	port := os.Getenv("PORT")
	session_key := os.Getenv("SESSION_KEY")
	key, err := base64.StdEncoding.DecodeString(session_key)
	if err != nil {
		log.Println("Error:", err)
		return
	}
	store := sessions.NewCookieStore(key)
	store.Options = &sessions.Options{MaxAge: 0}

	fs := http.FileServer(http.Dir("./static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) { handlerIndex(w, r, store) })
	http.HandleFunc("/flag", func(w http.ResponseWriter, r *http.Request) { handlerFlag(w, r, store) })
	http.HandleFunc("/login", func(w http.ResponseWriter, r *http.Request) { handlerLogin(w, r, store) })
	http.HandleFunc("/lang", func(w http.ResponseWriter, r *http.Request) { handlerLang(w, r, store) })

	log.Println("Starting the web server on port " + port)
	err = http.ListenAndServe(":"+port, nil)
	if err != nil {
		log.Fatal("Error starting the web server: ", err)
	}
}
