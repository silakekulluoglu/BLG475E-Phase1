'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []

    smallest = min(numbers)
    largest = max(numbers)
    range_size = largest - smallest

    scaled = [(x - smallest) / range_size for x in numbers]
    return scaled