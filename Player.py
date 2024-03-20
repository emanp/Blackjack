#Class for the player and their moves

class Player():
    
    def __init__(self, hand):
        self.hand = hand
        self.playerMove = 0
        self.isLoser = False
        self.isBust = False
    
    
    def hit(self):
        self.hand.addCard()
        
        
    def stand(self):
        ...
    
    def makePlayerMove(self):
        self.playerMove = int(input())
        
        while True:
            if self.playerMove == 1:
                self.hit()
                return 1
                
            elif self.playerMove == 2:
                self.stand()
                return 2
            else:
                continue
            
            
    def checkIfBust(self):
        if self.hand.handValue > 21:
            self.isBust = True
        
        