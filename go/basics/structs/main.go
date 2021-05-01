<<<<<<< HEAD
package main

import (
	"fmt"
)

type contactInfo struct {
	email string
	zipCode int
}

type person struct {
	firstName string
	lastName  string
	contactInfo
}

func main() {
	// alex := person{firstName: "Alex", lastName: "Anderson"}
	// fmt.Println(alex)

	// var alex person
	// alex.firstName = "Alex"
	// alex.lastName = "Anderson"

	// fmt.Println(alex)
	// fmt.Printf("%+v", alex)

	erdem := person{
		firstName: "Erdem",
		lastName: "Bozdag",
		contactInfo: contactInfo{
			email: "ebozdag@gmail.com",
			zipCode: 93221,
		},
	}

	// erdemPointer := &erdem
	erdem.updateName("adam")
	erdem.print()
}

func (pointerToPerson *person) updateName(newFirstName string) {
	(*pointerToPerson).firstName = newFirstName
}

func (p person) print() {
	fmt.Printf("%+v", p)
}
=======
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
>>>>>>> 4a886dcbc59085a0f23c6c57ee07ddc5868e6f32
