package main

import "fmt"

type contactInfo struct {
	email string
	zipCode string
}

type person struct {
	firstName string
	lastName string
	contact contactInfo
}

func main() {
	// var alex person
	// alex.firstName = "Erdem"
	// alex.lastName = "Bozdag"
	// fmt.Println(alex)
	// fmt.Printf("%+v", alex)
	// alex = person{firstName:"Alex",lastName:"Anderson"}
	jim := person{
		firstName: "Jim",
		lastName: "Party",
		contact: contactInfo{
			email: "jim@gmail.com",
			zipCode: "94000",
		},
	}

	// jim_pointer := &jim // adresing the memory adress
	jim.updateName("Jimmy")
	jim.print()
}

// Turn address into value with *adress
// Turn value into address with &value
func (jim_pointer *person) updateName(firstName string) { // the pointer points a person
	(*jim_pointer).firstName = firstName // manipulate the value the pointer is referencing
}

func (p person) print() {
	fmt.Printf("%+v", p)
}