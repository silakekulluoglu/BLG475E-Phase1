'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/moderate')
    )
)


from human_eval_107 import even_odd_palindrome

import unittest

class TestEvenOddPalindrome(unittest.TestCase):
    def test_n_two(self):
        self.assertEqual(even_odd_palindrome(2), (1, 1))

    def test_n_zero(self):
        self.assertEqual(even_odd_palindrome(0), (0, 0))

    def test_upper_bound(self):
        ev, od = even_odd_palindrome(1000)
        self.assertIsInstance((ev, od), tuple)
        self.assertTrue(ev + od > 0)

if __name__ == '__main__':
    unittest.main()
