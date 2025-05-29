import unittest
from integration_testing.integration_classes.qwen2_5_coder_32b_instruct.number_processor import NumberProcessor

class TestNumberProcessor(unittest.TestCase):

    # --- Integration Tests ---

    def test_process_numbers_typical(self):
        processor = NumberProcessor([4, 6, 8])
        self.assertEqual(processor.process_numbers(), [0.0, 1.0])

    def test_process_numbers_all_divisible(self):
        processor = NumberProcessor([2, 4, 6])
        self.assertEqual(processor.process_numbers(), [0.0, 1.0])

    def test_process_numbers_pluck_zero(self):
        processor = NumberProcessor([0, 2, 4])
        self.assertEqual(processor.process_numbers(), [0.0, 1.0])

    def test_process_numbers_all_same(self):
        processor = NumberProcessor([4, 4])
        with self.assertRaises(ValueError):
            processor.process_numbers()

    def test_process_numbers_single_element(self):
        processor = NumberProcessor([8])
        with self.assertRaises(ValueError):
            processor.process_numbers()

    def test_process_numbers_empty(self):
        processor = NumberProcessor([])
        with self.assertRaises(ValueError):
            processor.process_numbers()

    def test_process_numbers_no_even(self):
        processor = NumberProcessor([3, 9, 15])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])

    def test_process_numbers_mixed_divisible_and_not(self):
        processor = NumberProcessor([6, 9, 12, 15])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])

    def test_process_numbers_unordered_input(self):
        processor = NumberProcessor([10, 4, 8, 2])
        result = processor.process_numbers()
        expected = [1.0, 0.0, 0.6666666666666666]
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b)

    def test_process_numbers_with_negatives(self):
        processor = NumberProcessor([6, -12, -18, 3])
        with self.assertRaises(ValueError):
            processor.process_numbers()

    def test_process_numbers_all_coprime(self):
        processor = NumberProcessor([3, 5, 7])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])

    def test_process_numbers_gcd_filters_out_most(self):
        processor = NumberProcessor([10, 20, 33, 35])
        result = processor.process_numbers()
        expected = [0.0, 0.8666666666666667, 1.0]
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b)

    def test_process_numbers_gcd_excludes_extremes(self):
        processor = NumberProcessor([14, 28, 30, 35])
        result = processor.process_numbers()
        self.assertGreaterEqual(len(result), 2)
        self.assertAlmostEqual(min(result), 0.0)
        self.assertAlmostEqual(max(result), 1.0)

    def test_process_numbers_excludes_non_divisibles(self):
        processor = NumberProcessor([18, 24, 7, 36])
        result = processor.process_numbers()
        self.assertEqual(len(result), 3)
        self.assertAlmostEqual(min(result), 0.0)
        self.assertAlmostEqual(max(result), 1.0)

    def test_process_numbers_high_gcd(self):
        processor = NumberProcessor([20, 40, 60, 80])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])

    # --- pluck() tests ---

    def test_pluck_unique(self):
        processor = NumberProcessor([])
        self.assertEqual(processor.pluck([7, 5, 2]), [2, 2])

    def test_pluck_multiple_same(self):
        processor = NumberProcessor([])
        self.assertEqual(processor.pluck([2, 4, 2, 6]), [2, 0])

    def test_pluck_no_even(self):
        processor = NumberProcessor([])
        self.assertEqual(processor.pluck([1, 3, 5]), [])

    # --- gcd() tests ---

    def test_gcd_multiple(self):
        processor = NumberProcessor([])
        self.assertEqual(processor.greatest_common_divisor(12, 16), 4)

    def test_gcd_identity(self):
        processor = NumberProcessor([])
        self.assertEqual(processor.greatest_common_divisor(7, 7), 7)

    def test_gcd_one(self):
        processor = NumberProcessor([])
        self.assertEqual(processor.greatest_common_divisor(7, 9), 1)

    # --- rescale_to_unit() tests ---

    def test_rescale_varied(self):
        processor = NumberProcessor([])
        result = processor.rescale_to_unit([10, 20, 30])
        expected = [0.0, 0.5, 1.0]
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b)

    def test_rescale_identical(self):
        processor = NumberProcessor([])
        self.assertEqual(processor.rescale_to_unit([5, 5]), [0.0, 0.0])

    def test_rescale_empty(self):
        processor = NumberProcessor([])
        with self.assertRaises(ValueError):
            processor.rescale_to_unit([])

if __name__ == "__main__":
    unittest.main()
