#Emanuelle Pelayo
#CS 333 Homework #2
#Feb. 21st, 2024

#This blackjack game assumes that Aces are worth 1 point and assumes that a tie is a win 
#for the player. What a nice dealer!




from Player import Player
from Dealer import Dealer
from Deck import Deck
from Game import Game
from Hand import Hand 


def main():
    deck = Deck()
    playerHand = Hand(deck)
    dealerHand = Hand(deck)
    
    player = Player(playerHand)
    dealer = Dealer(dealerHand)
    game = Game(player, dealer, deck)
    game.playGame()
    
    
if __name__ == "__main__":
    main()
    
    