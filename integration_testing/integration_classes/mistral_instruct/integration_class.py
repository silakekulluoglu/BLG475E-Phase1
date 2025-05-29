from typing import List

class DataAnalysis:
    def __init__(self):
        pass

    # Greatest Common Divisor (GCD) function using Euclidean algorithm
    def greatest_common_divisor(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # Rescale a list of numbers such that the smallest number will become 0 and the largest will become 1
    def rescale_to_unit(self, numbers: List[float]) -> List[float]:
        min_number = min(numbers)
        max_number = max(numbers)
        return [(x - min_number) / (max_number - min_number) for x in numbers]

    # Pluck one node from an array representing a branch of a tree that has non-negative integer nodes
    def pluck(self, arr):
        if len(arr) == 0: return []
        evens = list(filter(lambda x: x%2 == 0, arr))
        if not evens: return []
        return [min(evens), arr.index(min(evens))]