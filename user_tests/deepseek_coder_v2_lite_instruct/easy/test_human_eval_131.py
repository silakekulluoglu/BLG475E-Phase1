'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/easy')
    )
)


from human_eval_131 import digits


import unittest

class TestDigits(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(digits(0), 0)

    def test_all_odd(self):
        self.assertEqual(digits(13579), 945)

    def test_mixed_digits(self):
        self.assertEqual(digits(10203), 3)

    def test_repeated_digits(self):
        self.assertEqual(digits(111111), 1)

    def test_no_odd_digits(self):
        self.assertEqual(digits(2468), 0)

    def test_large_number(self):
        self.assertEqual(digits(9876543210), 945)

if __name__ == "__main__":
    unittest.main()
