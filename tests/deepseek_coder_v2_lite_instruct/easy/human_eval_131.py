import unittest

class TestDigits(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(digits(5), 5)
        self.assertEqual(digits(54), 5)
        self.assertEqual(digits(120), 1)
        self.assertEqual(digits(5014), 5)
    
    def test_edge_cases(self):
        self.assertEqual(digits(2468), 0)

if __name__ == '__main__':
    unittest.main()
