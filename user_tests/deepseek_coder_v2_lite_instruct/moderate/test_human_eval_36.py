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
            '../../../../source/deepseek_coder_v2_lite_instruct/moderate'
        )
    )
)


from human_eval_36 import fizz_buzz

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_n_less_than_eleven(self):
        self.assertEqual(fizz_buzz(10), 0)

    def test_n_zero(self):
        self.assertEqual(fizz_buzz(0), 0)

    def test_exact_multiple(self):
        self.assertEqual(fizz_buzz(11), 0)  

    def test_large_n(self):
        result = fizz_buzz(1000)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        
if __name__ == '__main__':
    unittest.main()
