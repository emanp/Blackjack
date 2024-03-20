#Tests for Card.py


import unittest 

from Card import Card

class Test_Card(unittest.TestCase):

	def test_init_non_empty_rank(self):
		self.card = Card("A")
		self.assertEqual(self.card.rank, "A")
  
  

if __name__ == "__main__":
    unittest.main()

