'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Union
from regenerated_codes.mistral_instruct.hard.human_eval_94 import skjkasdkd

class TestSkjkasdkd(unittest.TestCase):
    def test_given_examples(self):
        self.assertEqual(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
        self.assertEqual(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
        self.assertEqual(skjkasdkd([0,81,12,3,1,21]), 3)
        self.assertEqual(skjkasdkd([0,8,1,2,1,7]), 7)

    def test_empty_list(self):
        self.assertEqual(skjkasdkd([]), 0)

    def test_no_primes(self):
        self.assertEqual(skjkasdkd([0, 1, 4, 6, 8, 9, 10, 12, 15]), 0)

    def test_single_prime(self):
        self.assertEqual(skjkasdkd([13]), 4)

    def test_all_same_prime(self):
        self.assertEqual(skjkasdkd([7, 7, 7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(skjkasdkd([-3, -2, -5, -7, 2, 3]), 3)

    def test_large_prime(self):
        self.assertEqual(skjkasdkd([99991, 104729]), 23)  # 104729 is a known large prime; 1+0+4+7+2+9 = 23

    def test_mixed_types(self):
        self.assertEqual(skjkasdkd([4, 6, 3, 5, 7]), 7)  # max prime is 7