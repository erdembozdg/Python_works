package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)


type Customer struct {
	Name string  `json:"full_name"`
	City string  `json:"city"`
	ZipCode string  `json:"zip_code"`
}

func greet(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprint(rw, "Hello World!!")
}

func getAllCustomers(rw http.ResponseWriter, r *http.Request) {
	customers := []Customer {
		{"Erdem", "Vancouver", "12345"},
		{"Sinem", "Istanbul", "54321"},
	}
	rw.Header().Add("Content-Type", "application/json")
	json.NewEncoder(rw).Encode(customers)
}