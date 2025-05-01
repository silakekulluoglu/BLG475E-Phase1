'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_131 import digits

class TestDigits(unittest.TestCase):
    def test_digits_1(self):
        self.assertEqual(digits(5), 5)

    def test_digits_2(self):
        self.assertEqual(digits(54), 5)

    def test_digits_3(self):
        self.assertEqual(digits(120), 1)

    def test_digits_4(self):
        self.assertEqual(digits(5014), 5)

    def test_digits_5(self):
        self.assertEqual(digits(2468), 0)

if __name__ == '__main__':
    unittest.main()