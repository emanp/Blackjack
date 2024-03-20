#Class for the player and dealer's hands during the game

class Hand():
    
    def __init__(self, deck):
        self.cards = []
        self.handValue = 0 
        self.deck = deck
        
    def updateHandValue(self):
        self.handValue = 0
        for card in self.cards:
            if card.rank == "A":
                self.handValue = self.handValue + 1
            elif card.rank in ["J", "Q", "K"]:
                self.handValue = self.handValue + 10
            else:
                cardValue = int(card.rank)
                self.handValue = self.handValue + cardValue
        
        return self.handValue
        
    def addCard(self):
        self.cards.append(self.deck.dealCard())
        self.updateHandValue()
        
    def handAsString(self):
        
        hand = ""
        for card in self.cards:
            hand = hand + " " + card.rank
            
        return hand
        