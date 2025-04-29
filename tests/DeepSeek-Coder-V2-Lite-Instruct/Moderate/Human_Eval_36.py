import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(fizz_buzz(50), 0)
    
    def test_case_2(self):
        self.assertEqual(fizz_buzz(78), 2)
    
    def test_case_3(self):
        self.assertEqual(fizz_buzz(79), 3)
    
    def test_case_4(self):
        self.assertEqual(fizz_buzz(100), 3)
    
    def test_case_5(self):
        self.assertEqual(fizz_buzz(200), 6)

if __name__ == '__main__':
    unittest.main()
