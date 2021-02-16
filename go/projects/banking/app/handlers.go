package app

import (
	"encoding/json"
	"fmt"
	"net/http"
	"github.com/erdembozdg/coding/go/projects/banking/service"
	"github.com/gorilla/mux"
)

type Customer struct {
	Name string  `json:"full_name"`
	City string  `json:"city"`
	ZipCode string  `json:"zip_code"`
}

type Customerhandlers struct {
	service service.CustomerSerive
}

func (ch *Customerhandlers) getAllCustomers(rw http.ResponseWriter, r *http.Request) {
	customers, _ := ch.service.GetAllCustomer()
	rw.Header().Add("Content-Type", "application/json")
	json.NewEncoder(rw).Encode(customers)
}

func getCustomer(rw http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	fmt.Fprint(rw, vars["customer_id"])
}

func createCustomer(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprint(rw, "Post request received")
}

func greet(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprint(rw, "Hello World!!")
}