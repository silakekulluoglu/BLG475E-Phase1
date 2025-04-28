import unittest

class TestBf(unittest.TestCase):
    def test_bf_1(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_bf_2(self):
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))

    def test_bf_3(self):
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_bf_4(self):
        self.assertEqual(bf("Neptune", "Venus"), ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

    def test_bf_5(self):
        self.assertEqual(bf("Earth", "Earth"), ())

if __name__ == '__main__':
    unittest.main()