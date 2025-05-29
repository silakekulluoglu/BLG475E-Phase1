import unittest
from typing import List
from integration_testing.integration_classes.mistral_instruct.integration_class import DataAnalysis

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        self.data = DataAnalysis()
        self.candidate = DataAnalysis()

    def test_greatest_common_divisor(self):
        self.assertEqual(self.candidate.greatest_common_divisor(3, 7), self.data.greatest_common_divisor(3, 7))
        self.assertEqual(self.candidate.greatest_common_divisor(10, 15), self.data.greatest_common_divisor(10, 15))
        self.assertEqual(self.candidate.greatest_common_divisor(49, 14), self.data.greatest_common_divisor(49, 14))
        self.assertEqual(self.candidate.greatest_common_divisor(144, 60), self.data.greatest_common_divisor(144, 60))

    def test_rescale_to_unit(self):
        self.assertEqual(self.candidate.rescale_to_unit([2.0, 49.9]), self.data.rescale_to_unit([2.0, 49.9]))
        self.assertEqual(self.candidate.rescale_to_unit([100.0, 49.9]), self.data.rescale_to_unit([100.0, 49.9]))
        self.assertEqual(self.candidate.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), self.data.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
        self.assertEqual(self.candidate.rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]), self.data.rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]))
        self.assertEqual(self.candidate.rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]), self.data.rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]))

    def test_pluck(self):
        self.assertEqual(self.candidate.pluck([4,2,3]), self.data.pluck([4,2,3]))
        self.assertEqual(self.candidate.pluck([1,2,3]), self.data.pluck([1,2,3]))
        self.assertEqual(self.candidate.pluck([]), self.data.pluck([]))
        self.assertEqual(self.candidate.pluck([5, 0, 3, 0, 4, 2]), self.data.pluck([5, 0, 3, 0, 4, 2]))
        self.assertEqual(self.candidate.pluck([1, 2, 3, 0, 5, 3]), self.data.pluck([1, 2, 3, 0, 5, 3]))
        self.assertEqual(self.candidate.pluck([5, 4, 8, 4 ,8]), self.data.pluck([5, 4, 8, 4 ,8]))
        self.assertEqual(self.candidate.pluck([7, 6, 7, 1]), self.data.pluck([7, 6, 7, 1]))
        self.assertEqual(self.candidate.pluck([7, 9, 7, 1]), self.data.pluck([7, 9, 7, 1]))

