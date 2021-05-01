package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) != 12 {
		t.Errorf("Expected deck length of 20, but got %v", len(d))
	}

	if d[0] != "Ace of Spades" {
		t.Errorf("Expected first card of Ace, but got %v", d[0])
	}

	if d[len(d)-1] != "Three of Clubs" {
		t.Errorf("Expected last card of Three, but got %v", d[len(d)-1])
	}
}

func TestSaveAndRead(t *testing.T) {
	os.Remove("_decktesting")

	deck := newDeck()
	deck.savetoFile("_decktesting")

	loadedDeck := newDecFromFile("_decktesting")

	if len(loadedDeck) != 12 {
		t.Errorf("Expected deck length of 20, but got %v", len(loadedDeck))
	}

	os.Remove("_decktesting")
}
