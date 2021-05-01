package main

import "fmt"

func main() {
	colors := map[string]string {
		"red": "#12345",
		"blue": "#43215",
		"green": "#87652",
	}

	// var colors map[string]string
	// colors := make(map[string]string)
	// colors["white"] = "#23412"
	// delete(colors, "white")
	printMap(colors)

}

func printMap(c map[string]string) {
	for color, value := range c {
		fmt.Println("Hex code for", color, "is", value)
	}
}