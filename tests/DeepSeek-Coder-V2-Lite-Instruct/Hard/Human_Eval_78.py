import unittest

class TestHexKey(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(hex_key("AB"), 1)
        self.assertEqual(hex_key("1077E"), 2)
        self.assertEqual(hex_key("ABED1A33"), 4)
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)
    
    def test_edge_cases(self):
        self.assertEqual(hex_key(""), 0)

if __name__ == '__main__':
    unittest.main()
