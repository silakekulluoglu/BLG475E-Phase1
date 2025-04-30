import unittest
from source.mistral_instruct.easy.human_eval_125 import split_words

class TestSplitWords(unittest.TestCase):
    def test_split_words(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("abcdef"), 3)
        self.assertEqual(split_words("z"), 0)
        self.assertEqual(split_words("abc"), 1)
        self.assertEqual(split_words("1abcdef"), 3)
        self.assertEqual(split_words("1abc1"), 1)
        self.assertEqual(split_words("1abc1z"), 1)
        self.assertRaises(TypeError, split_words, 123)

if __name__ == '__main__':
    unittest.main()