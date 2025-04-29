import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_75 import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):
    def test_is_multiply_prime_1(self):
        self.assertEqual(is_multiply_prime(5), False)

    def test_is_multiply_prime_2(self):
        self.assertEqual(is_multiply_prime(30), True)

    def test_is_multiply_prime_3(self):
        self.assertEqual(is_multiply_prime(8), False)

    def test_is_multiply_prime_4(self):
        self.assertEqual(is_multiply_prime(10), False)

    def test_is_multiply_prime_5(self):
        self.assertEqual(is_multiply_prime(125), False)

if __name__ == '__main__':
    unittest.main()