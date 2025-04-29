import unittest

class TestFindClosestElements(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]), (3.9, 4.0))
    
    def test_case_2(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]), (5.0, 5.9))
    
    def test_case_3(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
    
    def test_case_4(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
    
    def test_case_5(self):
        self.assertEqual(find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1]), (2.2, 3.1))

if __name__ == '__main__':
    unittest.main()
