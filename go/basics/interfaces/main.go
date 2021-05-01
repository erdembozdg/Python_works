package main

import "fmt"

type bot interface {
	getGreeting() string
}

type englisgBot struct{}
type spanishBot struct{}

func main() {
	eb := englisgBot{}
	sb := spanishBot{}

	printGreeting(eb)
	printGreeting(sb)
}

func printGreeting(b bot) {
	fmt.Println(b.getGreeting())
}

func (englisgBot) getGreeting() string {
	return "Hi There!!"
}

func (spanishBot) getGreeting() string {
	return "Hi Hola!!"
}