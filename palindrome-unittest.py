import unittest
from palindrome import isPalindrome

class PalindromeTest(unittest.TestCase):
    def test_basic_string(self):
        self.assertTrue(isPalindrome('racecar'))
    
    def test_number(self):
        self.assertRaises(TypeError, isPalindrome, 12321)
    
    def test_mixed_cases(self):
        self.assertFalse(isPalindrome('raCecAR'))
        

if __name__ == '__main__':
    unittest.main()