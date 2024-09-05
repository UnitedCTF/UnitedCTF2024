package main

import (
	"database/sql"
	"encoding/base64"
	"errors"
	"html/template"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"time"

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

func handlerLibrary(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) {
	serveTemplate(w, r, store, "library.html", nil)
}

func handlerIndex(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) {
	http.Redirect(w, r, "/library", http.StatusSeeOther)
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

func handlerLogin(w http.ResponseWriter, r *http.Request, db *sql.DB, store *sessions.CookieStore) {
	if r.Method == "POST" {
		username := r.FormValue("username")
		password := r.FormValue("password")

		log.Println("username: ", username, "\tPassword: ", password)
		id, err := getUserID(db, username)
		if err != nil {
			log.Println("Error:", err)
			return
		}
		if checkUser(db, id, password) {
			session, _ := store.Get(r, "session-name")
			_ = setChangeHash(db, id, password)

			session.Values["userid"] = id
			session.Values["is_admin"] = isAdministrator(db, id)
			err = session.Save(r, w)
			if err != nil {
				log.Println("Error:", err)
				return
			}
			http.Redirect(w, r, "/profile", http.StatusSeeOther)
			return
		} else {
			http.Redirect(w, r, "/login?invalidCredentials", http.StatusSeeOther)
		}
	} else {
		serveTemplate(w, r, store, "login.html", nil)
	}
}

func handlerRegister(w http.ResponseWriter, r *http.Request, db *sql.DB, store *sessions.CookieStore) {
	if r.Method == "POST" {
		username := r.FormValue("username")
		password := r.FormValue("password")
		name := r.FormValue("name")
		email := r.FormValue("email")

		log.Println("username: ", username, "\tPassword: ", password, "\tName: ", name, "\tEmail: ", email)

		id, err := getUserID(db, username)
		if errors.Is(err, sql.ErrNoRows) {
			err = createUser(db, username, password, email, name)
			if err != nil {
				return
			}
			http.Redirect(w, r, "/login", http.StatusSeeOther)
			return
		} else {
			http.Redirect(w, r, "/register?invalidCredentials="+strconv.Itoa(id), http.StatusSeeOther)
			return
		}
	} else {
		serveTemplate(w, r, store, "register.html", nil)
	}
}

func handlerLogout(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) {
	session, err := store.Get(r, "session-name")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	session.Values["userid"] = nil
	err = session.Save(r, w)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	http.Redirect(w, r, "/", http.StatusSeeOther)
}

func handlerProfile(w http.ResponseWriter, r *http.Request, db *sql.DB, store *sessions.CookieStore) {
	userid, err := getUserFromSession(w, r, store)
	if userid == nil || err != nil {
		http.Redirect(w, r, "/login", http.StatusSeeOther)
		return
	}

	name, email, _ := getUserInfo(db, userid.(int))
	userInfo := map[string]interface{}{}
	userInfo["Name"] = name
	userInfo["Email"] = email

	if isAdmin(store, r) {
		algorithms, err2 := getAlgorithms(db)
		if err2 != nil {
			return
		}
		userInfo["Algorithms"] = algorithms
	}
	serveTemplate(w, r, store, "profile.html", userInfo)
}

func changePassword(w http.ResponseWriter, r *http.Request, db *sql.DB, store *sessions.CookieStore) {
	userid, err := getUserFromSession(w, r, store)
	if userid == nil || err != nil {
		http.Redirect(w, r, "/login", http.StatusSeeOther)
		return
	}

	newPassword := r.FormValue("newPassword")
	err = setPassword(db, userid.(int), newPassword)
	if err != nil {
		return
	}

	http.Redirect(w, r, "/logout", http.StatusSeeOther)
}

func changeHash(w http.ResponseWriter, r *http.Request, db *sql.DB, store *sessions.CookieStore) {
	userid, err := strconv.Atoi(r.FormValue("userid"))
	if err != nil {
		return
	}

	algoId, err := strconv.Atoi(r.FormValue("algoid"))
	if err != nil {
		return
	}

	_, _, err = getUserInfo(db, userid)
	if err != nil {
		return
	}

	algos, err := getAlgorithms(db)
	if err != nil {
		return
	}

	ispresent := false
	for algo := range algos {
		if algos[algo]["id"] == algoId {
			ispresent = true
			break
		}
	}

	if !ispresent {
		return
	}

	err = addChangeHash(db, userid, algoId)
	if err != nil {
		return
	}

	http.Redirect(w, r, "/profile?updatedHash", http.StatusSeeOther)
}

func getUserFromSession(w http.ResponseWriter, r *http.Request, store *sessions.CookieStore) (interface{}, error) {
	session, err := store.Get(r, "session-name")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return "", err
	}

	userid := session.Values["userid"]

	return userid, nil
}

func isLogged(store *sessions.CookieStore, r *http.Request) bool {
	session, err := store.Get(r, "session-name")
	if err != nil {
		return false
	}

	userid := session.Values["userid"]
	if userid == nil {
		return false
	}

	return true
}

func isAdmin(store *sessions.CookieStore, r *http.Request) bool {
	session, err := store.Get(r, "session-name")
	if err != nil {
		return false
	}

	userid := session.Values["userid"]
	if userid == nil {
		return false
	}

	admin := session.Values["is_admin"]
	if admin == nil {
		return false
	}
	return admin.(bool)
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
	data["IsAdmin"] = isAdmin(store, r)
	data["Lang"] = lang

	// Execute the "layout" template
	err = tmpl.ExecuteTemplate(w, "layout", data)

	// Check for errors when executing the template
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func main() {
	key, err := base64.StdEncoding.DecodeString(os.Getenv("SESSION_KEY"))
	if err != nil {
		log.Println("Error:", err)
		return
	}
	store := sessions.NewCookieStore(key)
	store.Options = &sessions.Options{MaxAge: 0}

	var db *sql.DB
	for {
		db, err = createConnection()
		if err != nil {
			log.Println("Error:", err)
			time.Sleep(3 * time.Second)
		} else {
			break
		}
	}

	fs := http.FileServer(http.Dir("./static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) { handlerIndex(w, r, store) })
	http.HandleFunc("/login", func(w http.ResponseWriter, r *http.Request) { handlerLogin(w, r, db, store) })
	http.HandleFunc("/logout", func(w http.ResponseWriter, r *http.Request) { handlerLogout(w, r, store) })
	http.HandleFunc("/register", func(w http.ResponseWriter, r *http.Request) { handlerRegister(w, r, db, store) })
	http.HandleFunc("/profile", func(w http.ResponseWriter, r *http.Request) { handlerProfile(w, r, db, store) })
	http.HandleFunc("/library", func(w http.ResponseWriter, r *http.Request) { handlerLibrary(w, r, store) })
	http.HandleFunc("/changeHash", func(w http.ResponseWriter, r *http.Request) { changeHash(w, r, db, store) })
	http.HandleFunc("/changePassword", func(w http.ResponseWriter, r *http.Request) { changePassword(w, r, db, store) })
	http.HandleFunc("/lang", func(w http.ResponseWriter, r *http.Request) { handlerLang(w, r, store) })

	port := os.Getenv("PORT")
	err = http.ListenAndServe(":"+port, nil)
	if err != nil {
		log.Fatalf("Server failed to start: %v", err)
		return
	}
}
