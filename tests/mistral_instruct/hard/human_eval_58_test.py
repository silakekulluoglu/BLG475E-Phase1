import unittest
from typing import List
from source.mistral_instruct.hard.human_eval_58 import common

class TestCommon(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_empty_lists(self):
        self.assertListEqual(common([]), [])
        self.assertListEqual(common([], [1, 2, 3]), [])

    def test_identical_lists(self):
        self.assertListEqual(common([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_single_elements(self):
        self.assertListEqual(common([1], [2, 1]), [1])
        self.assertListEqual(common([2, 1], [1]), [1])

    def test_same_but_different_order(self):
        self.assertListEqual(common([2, 1], [1, 2]), [1, 2])

    def test_multiple_elements(self):
        self.assertListEqual(common([1, 2, 3, 4], [4, 5, 6, 1, 2]), [1, 2])