package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	//routes
	http.HandleFunc("/greet", greet)

	//starting server
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

func greet(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprint(rw, "Hello World!!")
}