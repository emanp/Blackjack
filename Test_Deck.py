#tests for Deck.py -- DONE

import unittest 

from Deck import Deck

class Test_Deck(unittest.TestCase):
    
    #integration, conditional, functional tests for makeDeck
    def test_makeDeck(self): #DONE
        deck = Deck()
        deck.makeDeck()
        
        numRankInstancesInDeck = 0 
        for card in deck.deck:
            if card.rank == "A":
                numRankInstancesInDeck = numRankInstancesInDeck + 1
        
        self.assertEqual(numRankInstancesInDeck, 4)
        self.assertEqual(deck.deck[0].rank, "A")
        self.assertEqual(deck.deck[51].rank, "K")
        self.assertEqual (len(deck.deck), 52)
        
    def test_makeDeck_deck_is_not_empty(self): #DONE
        deck = Deck()
        
        self.assertIsNone(deck.makeDeck())
        
    #------------------------TODO----------------------
        
    def test_shuffleCards(self): #Done
        deck = Deck()
        unShuffledDeck = deck.deck
        
        deck.makeDeck()
        shuffledDeck = deck.shuffleCards()
        self.assertNotEqual(deck.deck, shuffledDeck)
        
    def test_dealCard_deck_not_empty(self):
        deck = Deck()
        deck.makeDeck()
        
        self.assertEqual("K", deck.dealCard().rank)
    
    def test_dealCard_deck_is_empty(self): #done
        deck = Deck()
        
        self.assertIsNone(deck.dealCard()) #returns None otherwise
        
if __name__ == "__main__":
    unittest.main()    
        
        
        
        
        
        
        