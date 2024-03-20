#Class for the deck of cards that the game will use


from Card import Card
import random #for shuffling cards


class Deck():
    def __init__(self):
        self.deck = []
        self.numCards = 0
        
    
    def makeDeck(self): #initialize the deck with 52 cards, 4 of each rank
        
        if not self.deck: #if the deck is empty
            cardRanks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
            
            for rank in cardRanks:
                card = Card(rank)
                self.deck.append(card)
            self.numCards = len(self.deck)
    
    def shuffleCards(self):#shuffles the cards in the deck[]
        random.shuffle(self.deck)
        
    def dealCard(self):
        
        indexToGrabCardFrom = len(self.deck) - 1
        
        if not len(self.deck) == 0: #if the deck is not empty
            cardDealt = self.deck[indexToGrabCardFrom]#store the card in a variable
            self.deck.remove(cardDealt)#remove the card from the deck
            self.numCards = self.numCards - 1 #decrement number of cards
            
            return cardDealt #return the card 
            
    
