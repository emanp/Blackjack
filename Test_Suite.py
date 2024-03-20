#Test suite

import unittest 

from Test_Card import Test_Card
from Test_Dealer import Test_Dealer
from Test_Deck import Test_Deck
from Test_Game import Test_Game
from Test_Hand import Test_Hand
from Test_Player import Test_Player


def suite():
    testloader = unittest.TestLoader()
    suite = unittest.TestSuite
    
    #Adding tests to the test suite
    suite.addTests(testloader.loadTestsFromTestCase(Test_Card))
    suite.addTests(testloader.loadTestsFromTestCase(Test_Dealer))
    suite.addTests(testloader.loadTestsFromTestCase(Test_Deck))
    suite.addTests(testloader.loadTestsFromTestCase(Test_Game))
    suite.addTests(testloader.loadTestsFromTestCase(Test_Hand))
    suite.addTests(testloader.loadTestsFromTestCase(Test_Player))
    
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())