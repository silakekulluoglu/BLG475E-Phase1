import unittest
from source.mistral_instruct.easy.human_eval_131 import digits

class TestDigits(unittest.TestCase):
    def test_digits(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(1234), 0)
        self.assertRaises(TypeError, digits, "abc")
        self.assertRaises(ValueError, digits, -1)

if __name__ == '__main__':
    unittest.main()