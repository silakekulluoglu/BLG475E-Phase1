'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_121 import solution

class TestSolution(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)

    def test_solution_2(self):
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)

    def test_solution_3(self):
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    def test_solution_4(self):
        self.assertEqual(solution([5, 9]), 5)

    def test_solution_5(self):
        self.assertEqual(solution([30, 13, 23, 32]), 23)

if __name__ == '__main__':
    unittest.main()