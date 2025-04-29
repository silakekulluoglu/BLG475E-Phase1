import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_10 import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    def test_make_palindrome_1(self):
        self.assertEqual(make_palindrome(''), '')

    def test_make_palindrome_2(self):
        self.assertEqual(make_palindrome('x'), 'x')

    def test_make_palindrome_3(self):
        self.assertEqual(make_palindrome('xyz'), 'xyzyx')

    def test_make_palindrome_4(self):
        self.assertEqual(make_palindrome('xyx'), 'xyx')

    def test_make_palindrome_5(self):
        self.assertEqual(make_palindrome('jerry'), 'jerryrrej')

if __name__ == '__main__':
    unittest.main()