import unittest

class TestEncode(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(encode('TEST'), 'tgst')
        self.assertEqual(encode('Mudasir'), 'mWDCSKR')
        self.assertEqual(encode('YES'), 'ygs')
    
    def test_edge_cases(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode("I DoNt KnOw WhAt tO WrItE"), 'k dQnT kNqW wHcT Tq wRkTg')

if __name__ == '__main__':
    unittest.main()