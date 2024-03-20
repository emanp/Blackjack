#Tests for Player.py
#DONE
import unittest
from Player import Player
from Hand import Hand
from Deck import Deck
from Card import Card

class Test_Player(unittest.TestCase):
    
    def test_hit(self):
        deck = Deck()
        card = Card("A")
        deck.deck = [card]
        
        hand = Hand(deck)
        player = Player(hand)
        
        
        
        player.hit()
        
        self.assertEqual(player.hand.cards, [card])
        
        
    def test_stand(self):
        deck = Deck()
        hand = Hand(deck)
        
        player = Player(hand)
        self.assertIsNone(player.stand())
        
        
    def test_checkIfBust_value_over_21(self):
        deck = Deck()
        hand = Hand(deck)
        
        player = Player(hand)
        player.hand.handValue = 22
        player.checkIfBust()
        self.assertTrue (player.isBust)
        
        
    def test_checkIfBust_value_below_21(self):
        deck = Deck()
        hand = Hand(deck)
        
        player = Player(hand)
        player.hand.handValue = 20
        player.checkIfBust()
        self.assertFalse (player.isBust)
        
if __name__ == "__main__":
    unittest.main()      
        
        
        
        