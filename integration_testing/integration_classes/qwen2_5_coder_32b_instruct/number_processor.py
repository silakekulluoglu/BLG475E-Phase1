from typing import List, Union, Tuple

class NumberProcessor:
    def __init__(self, numbers: List[int]):
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("All elements must be integers.")
        self.numbers = numbers

    def greatest_common_divisor(self, a: int, b: int) -> int:
        """Given two integers `a` and `b`, return their greatest common divisor (GCD) using the Euclidean algorithm."""
        if a == 0 and b == 0:
            raise ValueError("Both inputs cannot be zero.")
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a

    def rescale_to_unit(self, numbers: List[float]) -> List[float]:
        """Given a list of numbers (of at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1."""
        if len(numbers) < 2:
            raise ValueError("The list must contain at least two elements.")
        min_number = min(numbers)
        max_number = max(numbers)
        if min_number == max_number:
            return [0.0] * len(numbers)
        return [(x - min_number) / (max_number - min_number) for x in numbers]

    def pluck(self, numbers: List[int]) -> Union[List[int], List]:
        """Given a list of non-negative integers, return the smallest even number in the list and its index in the format [value, index].
        If there are multiple occurrences of the smallest even number, return the one with the lowest index.
        If the list is empty or contains no even numbers, return an empty list."""
        if not numbers:
            return []
        smallest_even = None
        smallest_index = None
        for index, num in enumerate(numbers):
            if not isinstance(num, int) or num < 0:
                raise ValueError("All elements must be non-negative integers.")
            if num % 2 == 0:
                if smallest_even is None or num < smallest_even:
                    smallest_even = num
                    smallest_index = index
        if smallest_even is not None:
            return [smallest_even, smallest_index]
        return []

    def process_numbers(self) -> Union[List[int], List]:
        """Process the numbers by plucking, removing the plucked number, computing GCD, filtering, and rescaling."""
        if len(self.numbers) < 2:
            raise ValueError("The list must contain at least two elements.")
        
        # Step 1: Find the smallest even number and its index in the list
        pluck_result = self.pluck(self.numbers)
        
        if not pluck_result:
            # If no even number is found, return the pluck result
            return pluck_result
        
        # Step 2: Remove the smallest even number from the list
        smallest_even, smallest_index = pluck_result
        modified_numbers = self.numbers[:smallest_index] + self.numbers[smallest_index + 1:]
        
        # Step 3: Compute GCD of the first two numbers in the modified list
        if len(modified_numbers) < 2:
            raise ValueError("The list must contain at least two elements after removing the plucked number.")
        gcd_result = self.greatest_common_divisor(modified_numbers[0], modified_numbers[1])
        
        # Step 4: Filter the list to keep only multiples of the GCD
        filtered_numbers = [num for num in modified_numbers if num % gcd_result == 0]
        
        # Step 5: Rescale the filtered list
        if len(filtered_numbers) < 2:
            raise ValueError("The filtered list must contain at least two elements for rescaling.")
        rescaled_numbers = self.rescale_to_unit(filtered_numbers)
        
        return rescaled_numbers