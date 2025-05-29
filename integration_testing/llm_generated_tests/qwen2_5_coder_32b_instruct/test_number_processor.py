import unittest
from typing import List, Union, Tuple
from integration_testing.integration_classes.qwen2_5_coder_32b_instruct.number_processor import NumberProcessor

class TestNumberProcessor(unittest.TestCase):

    def test_gcd(self):
        processor = NumberProcessor([1, 2, 3])
        self.assertEqual(processor.greatest_common_divisor(48, 18), 6)
        self.assertEqual(processor.greatest_common_divisor(101, 103), 1)
        self.assertEqual(processor.greatest_common_divisor(0, 5), 5)
        self.assertEqual(processor.greatest_common_divisor(5, 0), 5)
        self.assertEqual(processor.greatest_common_divisor(-48, 18), 6)
        self.assertEqual(processor.greatest_common_divisor(48, -18), 6)
        with self.assertRaises(ValueError):
            processor.greatest_common_divisor(0, 0)

    def test_rescale_to_unit(self):
        processor = NumberProcessor([1, 2, 3])
        self.assertEqual(processor.rescale_to_unit([1.0, 2.0, 3.0]), [0.0, 0.5, 1.0])
        self.assertEqual(processor.rescale_to_unit([-1.0, 0.0, 1.0]), [0.0, 0.5, 1.0])
        self.assertEqual(processor.rescale_to_unit([5.0, 5.0, 5.0]), [0.0, 0.0, 0.0])
        with self.assertRaises(ValueError):
            processor.rescale_to_unit([1.0])

    def test_pluck(self):
        processor = NumberProcessor([1, 2, 3])
        self.assertEqual(processor.pluck([1, 2, 3]), [2, 1])
        self.assertEqual(processor.pluck([1, 3, 5]), [])
        self.assertEqual(processor.pluck([]), [])
        self.assertEqual(processor.pluck([0, 2, 4]), [0, 0])
        with self.assertRaises(ValueError):
            processor.pluck([-2, 2, 4])
        with self.assertRaises(ValueError):
            processor.pluck([1.0, 2.0, 3.0])

    def test_process_numbers(self):
        # Test with a list containing even numbers
        processor = NumberProcessor([4, 2, 8, 6])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])  # Plucked 2, GCD=2, filtered=[4, 8, 6], rescaled=[0.0, 0.5, 1.0]

        # Test with a list where no even numbers are present
        processor = NumberProcessor([1, 3, 5])
        self.assertEqual(processor.process_numbers(), [])

        # Test with a list containing only one even number
        processor = NumberProcessor([1, 2])
        self.assertEqual(processor.process_numbers(), [])

        # Test with a list where the smallest even number has multiple occurrences
        processor = NumberProcessor([4, 2, 8, 2, 6])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])  # Plucked 2, GCD=2, filtered=[4, 8, 2, 6], rescaled=[0.0, 0.5, 0.0, 1.0]

        # Test with a list where the smallest even number is the first element
        processor = NumberProcessor([2, 4, 6, 8])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])  # Plucked 2, GCD=2, filtered=[4, 6, 8], rescaled=[0.0, 0.5, 1.0]

        # Test with a list where the smallest even number is the last element
        processor = NumberProcessor([4, 6, 8, 2])
        self.assertEqual(processor.process_numbers(), [0.0, 0.5, 1.0])  # Plucked 2, GCD=2, filtered=[4, 6, 8], rescaled=[0.0, 0.5, 1.0]

        # Test with a list where all numbers are multiples of the same GCD
        processor = NumberProcessor([10, 20, 30, 40])
        self.assertEqual(processor.process_numbers(), [0.0, 0.3333333333333333, 0.6666666666666666, 1.0])

        # Test with a list where the GCD is 1 and filtering keeps all numbers
        processor = NumberProcessor([2, 3, 5, 7])
        self.assertEqual(processor.process_numbers(), [0.0, 0.3333333333333333, 0.6666666666666666, 1.0])

        # Test with a list that has the same minimum and maximum after filtering
        processor = NumberProcessor([4, 4, 4, 4])
        self.assertEqual(processor.process_numbers(), [])

        # Test with invalid input (non-integer elements)
        with self.assertRaises(ValueError):
            processor = NumberProcessor([1, '2', 3])

        # Test with invalid input (less than two elements)
        with self.assertRaises(ValueError):
            processor = NumberProcessor([1])
            processor.process_numbers()

        # Test with invalid input (negative integers)
        with self.assertRaises(ValueError):
            processor = NumberProcessor([-2, 2, 4])
            processor.process_numbers()

        # Test with invalid input (both inputs to GCD are zero)
        with self.assertRaises(ValueError):
            processor = NumberProcessor([0, 0])
            processor.process_numbers()

        # Test with a list where the filtered list has less than two elements
        processor = NumberProcessor([2, 3, 5])
        self.assertEqual(processor.process_numbers(), [])

if __name__ == '__main__':
    unittest.main()