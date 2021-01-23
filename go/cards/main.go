package main

func main() {
	// cards := newDeck()
	// cards.savetoFile("my_cards")	
	cards := newDecFromFile("my_cards")
	cards.print()
}
