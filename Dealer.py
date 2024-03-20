#Class for the dealer (Your opponent)

import random
from Player import Player


class Dealer(Player):
    
    def __init__(self, hand):
        self.hand = hand
        self.moveToMake = 0
        self.isLoser = False
        self.isBust = False
        
    def randomizeDealerMoves(self):
        self.moveToMake = random.randint(1,2)
    
    def makeMove(self):
        
        
        if self.hand.handValue == 17:
            self.stand()
            return "Stand"
        else:
            if self.moveToMake == 1:
                self.hit()
                self.randomizeDealerMoves()
                return "Hit"
            else:
                self.stand()
                self.randomizeDealerMoves()
                return "Stand"
    
        
        
    
    
    