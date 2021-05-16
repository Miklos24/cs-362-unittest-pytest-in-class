import unittest
from wordCount import getWordCount

class WordCountTest(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(getWordCount("Hi I'm Bob."), 3)
    
    def test_number(self):
        self.assertRaises(AttributeError, getWordCount, 1234)
    
    def test_extra_spaces(self):
        self.assertEqual(getWordCount("   Hi I'm     Bob.  "), 3)

if __name__ == '__main__':
    unittest.main()