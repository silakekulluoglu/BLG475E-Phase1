'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_36 import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_3(self):
        self.assertEqual(fizz_buzz(79), 3)

    def test_fizz_buzz_4(self):
        self.assertEqual(fizz_buzz(100), 3)

    def test_fizz_buzz_5(self):
        self.assertEqual(fizz_buzz(200), 6)

if __name__ == '__main__':
    unittest.main()