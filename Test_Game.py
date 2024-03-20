#tests for Game.py

import unittest 
from Game import Game 
from Player import Player
from Dealer import Dealer
from Deck import Deck
from Hand import Hand 

class Test_Game(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.playerHand = Hand(self.deck)
        self.dealerHand = Hand(self.deck)
        
        self.player = Player(self.playerHand)
        self.dealer = Dealer(self.dealerHand)
        self.game = Game(self.player, self.dealer, self.deck)
    
    def test_checkWinner_player_is_bust(self):
        self.player.isBust = True
        
        self.game.checkWinner(False)
        
        self.assertTrue(self.player.isLoser)
        
    def test_checkWinner_dealer_is_bust(self):
        self.dealer.isBust = True
        
        self.game.checkWinner(False)
        
        self.assertTrue(self.dealer.isLoser)
    
        
    def test_checkWinner_move_not_stand(self):
        
        #player hand value > dealer hand value
        deck = Deck()
        playerHand = Hand(deck)
        dealerHand = Hand(deck)
        
        player = Player(playerHand)
        dealer = Dealer(dealerHand)
        game = Game(player, dealer, deck)
        
        player.isBust = False
        dealer.isBust = False
        
        player.hand.handValue = 20 
        dealer.hand.handValue = 19
        
        game.checkWinner(False)
        self.assertEqual(dealer.isLoser, True)
        
        
        
        
    def test_checkWinner_move_is_stand(self):
        
        self.player.hand.handValue = 21
        self.dealer.hand.handValue = 0
        
    
    
    
if __name__ == "__main__":
    unittest.main()