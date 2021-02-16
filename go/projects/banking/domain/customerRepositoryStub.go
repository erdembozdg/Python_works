package domain

type CustomerRepositoryStub struct {
	customers []Customer
}

func (s CustomerRepositoryStub) FindAll() ([]Customer, error) {
	return s.customers, nil
}

func NewCustomerRepositoryStub() CustomerRepositoryStub {
	customers := []Customer {
		{Id: "1001", Name: "Erdem", City: "Vancouver", Zipcode:"123"},
		{Id: "1002", Name: "Sinem", City: "Istanbul", Zipcode: "321"},
	}

	return CustomerRepositoryStub{customers: customers}
}