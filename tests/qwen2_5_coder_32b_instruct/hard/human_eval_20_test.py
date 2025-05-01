'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_20 import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    def test_find_closest_elements_1(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_find_closest_elements_2(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]), (5.0, 5.9))

    def test_find_closest_elements_3(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_find_closest_elements_4(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_find_closest_elements_5(self):
        self.assertEqual(find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1]), (2.2, 3.1))

if __name__ == '__main__':
    unittest.main()