import unittest

class TestSkjkasdkd(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
    
    def test_edge_cases(self):
        self.assertEqual(skjkasdkd([8191]), 19)
        self.assertEqual(skjkasdkd([8191, 123456, 127, 7]), 19)

if __name__ == '__main__':
    unittest.main()