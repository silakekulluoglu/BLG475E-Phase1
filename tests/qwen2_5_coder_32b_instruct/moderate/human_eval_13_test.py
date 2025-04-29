import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_13 import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_greatest_common_divisor_1(self):
        self.assertEqual(greatest_common_divisor(3, 7), 1)

    def test_greatest_common_divisor_2(self):
        self.assertEqual(greatest_common_divisor(10, 15), 5)

    def test_greatest_common_divisor_3(self):
        self.assertEqual(greatest_common_divisor(49, 14), 7)

    def test_greatest_common_divisor_4(self):
        self.assertEqual(greatest_common_divisor(144, 60), 12)

    def test_greatest_common_divisor_5(self):
        self.assertEqual(greatest_common_divisor(100, 25), 25)

if __name__ == '__main__':
    unittest.main()