import unittest

class TestEncode(unittest.TestCase):
    def test_encode_1(self):
        self.assertEqual(encode('TEST'), 'tgst')

    def test_encode_2(self):
        self.assertEqual(encode('Mudasir'), 'mWDCSKR')

    def test_encode_3(self):
        self.assertEqual(encode('YES'), 'ygs')

    def test_encode_4(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    def test_encode_5(self):
        self.assertEqual(encode("I DoNt KnOw WhAt tO WrItE"), 'k dQnT kNqW wHcT tQ wRkTg')

if __name__ == '__main__':
    unittest.main()