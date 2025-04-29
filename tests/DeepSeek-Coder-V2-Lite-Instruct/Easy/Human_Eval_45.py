import unittest

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area_5_3(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_triangle_area_2_2(self):
        self.assertAlmostEqual(triangle_area(2, 2), 2.0)

    def test_triangle_area_10_8(self):
        self.assertAlmostEqual(triangle_area(10, 8), 40.0)

    def test_triangle_area_negative_values(self):
        with self.assertRaises(Exception):
            triangle_area(-5, 3)

    def test_triangle_area_zero_values(self):
        self.assertAlmostEqual(triangle_area(0, 3), 0.0)

if __name__ == "__main__":
    unittest.main()
