#Tests for Hand.py
#DONE
import unittest 

from Hand import Hand 
from Deck import Deck
from Card import Card

class Test_Hand(unittest.TestCase):
    def test_updateHandValue_rank_is_A(self):
        deck = Deck()
        hand = Hand(deck) 
        
        cardRanks = ["A"]*21
            
        for rank in cardRanks:
            card = Card(rank)
            hand.cards.append(card)
        
        self.assertEqual(hand.updateHandValue(), 21)


    def test_updateHandValue_rank_is_JQK(self):
        deck = Deck()
        hand = Hand(deck) 
        
        cardRanks = ["J"]
            
        for rank in cardRanks:
            card = Card(rank)
            hand.cards.append(card)
            
        self.assertEqual(hand.updateHandValue(), 10)
        
        cardRanks = ["Q"]
        hand.cards = []
            
        for rank in cardRanks:
            card = Card(rank)
            hand.cards.append(card)
            
        self.assertEqual(hand.updateHandValue(), 10)
        
        cardRanks = ["K"]
        hand.cards = []
            
        for rank in cardRanks:
            card = Card(rank)
            hand.cards.append(card)
            
        self.assertEqual(hand.updateHandValue(), 10)
        
        
    def test_updateHandValue_rank_is_num(self):
        deck = Deck()
        hand = Hand(deck) 
        
        cardRanks = ["2", "3", "4","5","6","7","8","9"]
            
        for rank in cardRanks:
            card = Card(rank)
            hand.cards.append(card)
            
        self.assertEqual(hand.updateHandValue(), 44)
        
    def test_addCard(self):
        deck = Deck()
        hand = Hand(deck)
        
        deck.deck = ["J", "K"]
        hand.cards = ["K"]
        
        self.assertEqual(hand.cards,[deck.dealCard()])
        
    def test_handAsString_single_card(self):
        deck = Deck()
        hand = Hand(deck)
        card = Card("A")
        
        hand.cards = [card]
        
        self.assertEqual(" A", hand.handAsString())
        
    def test_handAsString_no_cards(self):
        deck = Deck()
        hand = Hand(deck)
        
        self.assertEqual("", hand.handAsString())
    
    def test_handAsString_multiple_cards(self):
        deck = Deck()
        hand = Hand(deck)
        card1 = Card("A")
        card2 = Card("K")
        
        hand.cards = [card1, card2]
        
        self.assertEqual(" A K", hand.handAsString())
        
        
if __name__ == "__main__":
    unittest.main()     
        
        
        
    