import unittest
import math
from typing import List, Union
from source.mistral_instruct import poly, find_zero

class TestPolyAndZero(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_poly_linear(self):
        xs = [1.0, 2.0]
        self.assertEqual(poly(xs, 1), 3)

    def test_poly_quadratic(self):
        xs = [1.0, 2.0, 1.0]
        self.assertEqual(poly(xs, 1), 3)
        self.assertEqual(poly(xs, 2), 5)

    def test_poly_cubic(self):
        xs = [1.0, 2.0, 3.0, 1.0]
        self.assertEqual(poly(xs, 1), 4)
        self.assertEqual(poly(xs, 2), 11)
        self.assertEqual(poly(xs, 3), 20)

    def test_poly_zero(self):
        xs = [1.0, -1.0]
        with self.assertRaises(ValueError):
            find_zero(xs)

    def test_poly_no_root(self):
        xs = [2.0, 3.0]
        with self.assertRaises(ValueError):
            find_zero(xs)