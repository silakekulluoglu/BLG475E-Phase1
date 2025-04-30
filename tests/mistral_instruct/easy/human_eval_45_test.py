import unittest
from source.mistral_instruct.easy.human_eval_45 import triangle_area

class TestTriangleArea(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_triangle_area_zero_base(self):
        result = triangle_area(5.0, 0.0)
        self.assertEqual(result, 0.0)

    def test_triangle_area_zero_height(self):
        result = triangle_area(2.0, 0.0)
        self.assertEqual(result, 0.0)

    def test_triangle_area_valid_values(self):
        result = triangle_area(5.0, 3.0)
        expected_output = 15.0
        self.assertAlmostEqual(result, expected_output)

    def test_triangle_area_negative_base(self):
        with self.assertRaises(ValueError):
            triangle_area(-3.0, 4.0)

    def test_triangle_area_negative_height(self):
        with self.assertRaises(ValueError):
            triangle_area(5.0, -3.0)