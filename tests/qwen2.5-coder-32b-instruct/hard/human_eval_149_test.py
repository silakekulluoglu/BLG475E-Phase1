import unittest

class TestSortedListSum(unittest.TestCase):
    def test_sorted_list_sum_1(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    def test_sorted_list_sum_2(self):
        self.assertEqual(sorted_list_sum(["school", "AI", "asdf", "b"]), ["AI", "asdf", "school"])

    def test_sorted_list_sum_3(self):
        self.assertEqual(sorted_list_sum(["d", "b", "c", "a"]), [])

    def test_sorted_list_sum_4(self):
        self.assertEqual(sorted_list_sum(["d", "dcba", "abcd", "a"]), ["abcd", "dcba"])

    def test_sorted_list_sum_5(self):
        self.assertEqual(sorted_list_sum(["AI", "ai", "au"]), ["AI", "ai", "au"])

if __name__ == '__main__':
    unittest.main()