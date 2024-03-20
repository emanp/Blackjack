#Tests for Dealer.py
#DONE

import unittest 
from Dealer import Dealer
from Hand import Hand 
from Deck import Deck 

class Test_Dealer(unittest.TestCase):
    
    def test_makeMove_handValue_is_seventeen(self):
        deck = Deck()
        deck.makeDeck()
        hand = Hand(deck)
        dealer = Dealer(hand)
        
        dealer.hand.handValue = 17 
        
        self.assertEqual(dealer.makeMove(), "Stand")
        
    
    def test_makeMove_handValue_not_seventeen(self):
        deck = Deck()
        deck.makeDeck()
        hand = Hand(deck)
        dealer = Dealer(hand)
        
        dealer.hand.handValue = 0
        #moveToMake is 1 
        dealer.moveToMake = 1
        self.assertEqual(dealer.makeMove(), "Hit")
        
        
        # #movetoMake is 0
        dealer.moveToMake = 0
        self.assertEqual(dealer.makeMove(), "Stand")
        
        
        
        ...
  
  
     
    
if __name__ == "__main__":
    unittest.main()