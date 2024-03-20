#Class to control all gameplay, rules, and output to command line

class Game():
    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        
    def playerWantsToContinue(self):
    
        while True:
            userInput = (input("---Continue?--- \n1. Yes \n2. No \n"))
            
            try:
                userInput = int(userInput)
            
            except:
                print ("Invalid option...")
            else:
                if userInput == 1:
                    self.playGame()
                elif userInput == 2:
                    break
                else: 
                    continue
    
    def checkWinner(self, isStand):
        
        if self.player.isBust is True:
            self.player.isLoser = True
        if self.dealer.isBust is True:
            self.dealer.isLoser = True
            
        if not isStand:
            #winning conditions
            if (self.player.hand.handValue == 21 and self.dealer.hand.handValue > 21):
                self.dealer.isLoser = True
            elif (self.dealer.hand.handValue == 21 and self.player.hand.handValue > 21):
                self.player.isLoser = True
            elif (self.player.hand.handValue == 21 and self.dealer.hand.handValue == 21):
                self.dealer.isLoser = True
                self.player.isLoser = True
        
        else:
            if (self.player.hand.handValue > self.dealer.hand.handValue and self.player.isBust is False):
                self.dealer.isLoser = True
            elif (self.player.hand.handValue < self.dealer.hand.handValue and self.dealer.isBust is False):
                self.player.isLoser = True
    
    def printResults(self):
        print ("--------Results--------")
        print ( "Dealer: " + self.dealer.hand.handAsString()+ " | Value: " + str(self.dealer.hand.handValue))
        print ("You: " + self.player.hand.handAsString() + " | Value: " + str(self.player.hand.handValue))
        
    
    def playGame(self):
        
        self.deck.makeDeck() #make the deck
        self.deck.shuffleCards() #shuffle the deck
        
        for i in range(2): #start both players off with 2 cards
            self.player.hit()
            self.dealer.hit()
            
            
        while self.player.isBust is not True and self.dealer.isBust is not True:
            
            
            print ("--------Blackjack--------")
            print ( "Dealer: " + self.dealer.hand.handAsString()+ " | Value: " + str(self.dealer.hand.handValue))
            print ("   You: " + self.player.hand.handAsString() + " | Value: " + str(self.player.hand.handValue))
            print ("1: HIT")
            print ("2: STAND")
        
            playerMove = self.player.makePlayerMove()
            
            if playerMove == 2:
                break
            
            self.dealer.makeMove()
            
            self.dealer.checkIfBust()
            self.player.checkIfBust()
            
            winner = self.checkWinner(False)
            
        winner = self.checkWinner(True)
    
        if self.player.isLoser is True and self.dealer.isLoser is not True:
            if self.player.isBust is True:
                self.printResults()
                print ("BUST! You lose...")
                
            else:
                self.printResults()
                print("You lose...")
                  
        elif self.player.isLoser is False and self.dealer.isLoser is True:
            if self.dealer.isBust is True:
                self.printResults()
                print ("Dealer BUST! You Win!")
                
                
            else:
                self.printResults()
                print ("You win!")
        self.playerWantsToContinue()
                
                
        
        
            
                
                




        