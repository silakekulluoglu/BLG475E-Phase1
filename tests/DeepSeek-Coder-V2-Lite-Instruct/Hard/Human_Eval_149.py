import unittest

class TestSortedListSum(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["school", "AI", "asdf", "b"]), ["AI", "asdf", "school"])
        self.assertEqual(sorted_list_sum(["d", "b", "c", "a"]), [])
        self.assertEqual(sorted_list_sum(["d", "dcba", "abcd", "a"]), ["abcd", "dcba"])
        self.assertEqual(sorted_list_sum(["AI", "ai", "au"]), ["AI", "ai", "au"])

if __name__ == "__main__":
    unittest.main()