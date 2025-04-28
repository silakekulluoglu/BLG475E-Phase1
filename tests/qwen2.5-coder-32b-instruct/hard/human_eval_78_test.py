import unittest

class TestHexKey(unittest.TestCase):
    def test_hex_key_1(self):
        self.assertEqual(hex_key("AB"), 1)

    def test_hex_key_2(self):
        self.assertEqual(hex_key("1077E"), 2)

    def test_hex_key_3(self):
        self.assertEqual(hex_key("ABED1A33"), 4)

    def test_hex_key_4(self):
        self.assertEqual(hex_key("2020"), 2)

    def test_hex_key_5(self):
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

if __name__ == '__main__':
    unittest.main()