import unittest

class TestSplitWords(unittest.TestCase):
    def test_split_on_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
    
    def test_split_on_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
    
    def test_count_lowercase_even_order(self):
        self.assertEqual(split_words("abcdef"), 3)
        self.assertEqual(split_words("aaabb"), 2)
        self.assertEqual(split_words("aaaBb"), 1)

if __name__ == '__main__':
    unittest.main()
