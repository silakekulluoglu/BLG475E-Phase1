import unittest

class TestPluck(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
        self.assertEqual(pluck([1, 2, 3]), [2, 1])
    
    def test_edge_cases(self):
        self.assertEqual(pluck([]), [])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])
        self.assertEqual(pluck([1, 2, 3, 0, 5, 3]), [0, 3])

if __name__ == '__main__':
    unittest.main()
