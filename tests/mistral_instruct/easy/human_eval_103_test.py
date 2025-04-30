import unittest
from source.mistral_instruct.easy.human_eval_103 import rounded_avg

class TestRoundedAvg(unittest.TestCase):
    def test_rounded_avg(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), "-1")
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertRaises(ValueError, rounded_avg, 1.5, 5)
        self.assertRaises(ValueError, rounded_avg, -1, 5)
        self.assertRaises(ValueError, rounded_avg, 1, -5)

if __name__ == '__main__':
    unittest.main()