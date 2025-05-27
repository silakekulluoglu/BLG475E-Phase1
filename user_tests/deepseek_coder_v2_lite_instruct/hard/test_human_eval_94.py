'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.insert(0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../../../../source/deepseek_coder_v2_lite_instruct/hard'
        )
    )
)

from human_eval_94 import skjkasdkd

import unittest

class TestSkjkasdkd(unittest.TestCase):
    def test_no_primes(self):
        self.assertEqual(skjkasdkd([4,6,8,10]), 0)
    def test_single_prime(self):
        self.assertEqual(skjkasdkd([4,7,4]), 7)
    def test_multiple_primes(self):
        self.assertEqual(skjkasdkd([3,5,11,2]), 1+1)  
    def test_large_prime(self):
        self.assertEqual(skjkasdkd([13,29,17]), 2+9) 
    def test_primes_and_nonprimes(self):
        self.assertEqual(skjkasdkd([0,2,4,5,10,13]), 1+3)

if __name__ == '__main__':
    unittest.main()