import unittest

class TestGetPositive(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
    
    def test_all_positive(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
    
    def test_all_negative(self):
        self.assertEqual(get_positive([-1, -2, -4, -5, -6]), [])
    
    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])
    
    def test_zero_present(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == "__main__":
    unittest.main()
