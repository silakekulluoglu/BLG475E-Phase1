import unittest
import math
from source.qwen2_5_coder_32b_instruct.hard.human_eval_32 import find_zero

class TestFindZero(unittest.TestCase):
    def test_find_zero_1(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=4)

    def test_find_zero_2(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=4)

    def test_find_zero_3(self):
        self.assertAlmostEqual(find_zero([1, -3, 2]), 1.0, places=4)

    def test_find_zero_4(self):
        self.assertAlmostEqual(find_zero([2, -4, 2]), 1.0, places=4)

    def test_find_zero_5(self):
        self.assertAlmostEqual(find_zero([-1, 0, 1]), 0.0, places=4)

if __name__ == '__main__':
    unittest.main()