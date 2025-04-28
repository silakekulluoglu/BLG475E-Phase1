import unittest

class TestPluck(unittest.TestCase):
    def test_pluck_1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_pluck_2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])

    def test_pluck_3(self):
        self.assertEqual(pluck([]), [])

    def test_pluck_4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_pluck_5(self):
        self.assertEqual(pluck([1, 2, 3, 0, 5, 3]), [0, 3])

if __name__ == '__main__':
    unittest.main()