package app

import (
	"log"
	"net/http"

	"github.com/erdembozdg/coding/go/projects/banking/domain"
	"github.com/erdembozdg/coding/go/projects/banking/service"
	"github.com/gorilla/mux"
)

func Start() {
	router := mux.NewRouter()

	ch := Customerhandlers{service: service.NewCustomerService(domain.NewCustomerRepositoryStub())}

	router.HandleFunc("/customers", ch.getAllCustomers).Methods(http.MethodGet)

	//starting server
	log.Fatal(http.ListenAndServe("localhost:8000", router))
}