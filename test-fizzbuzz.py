import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        self.assertEqual(affiche(), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee...")

if __name__ == "__main__":
    unittest.main()
