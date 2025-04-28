import unittest

class TestGetPositive(unittest.TestCase):
    def test_get_positive_1(self):
        self.assertEqual(get_positive([-1, -2, 4, 5, 6]), [4, 5, 6])

    def test_get_positive_2(self):
        self.assertEqual(get_positive([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 3, 9, 123, 1])

    def test_get_positive_3(self):
        self.assertEqual(get_positive([-1, -2]), [])

    def test_get_positive_4(self):
        self.assertEqual(get_positive([]), [])

    def test_get_positive_5(self):
        self.assertEqual(get_positive([0, 1, -1, 2, -2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()