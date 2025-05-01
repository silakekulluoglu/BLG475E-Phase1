'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_98 import count_upper

class TestCountUpper(unittest.TestCase):
    def test_count_upper_1(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_count_upper_2(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_count_upper_3(self):
        self.assertEqual(count_upper('dBBE'), 0)

    def test_count_upper_4(self):
        self.assertEqual(count_upper('B'), 0)

    def test_count_upper_5(self):
        self.assertEqual(count_upper('U'), 1)

if __name__ == '__main__':
    unittest.main()