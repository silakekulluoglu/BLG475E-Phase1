'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

from typing import List
import math

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(set(numbers)) == 1:
        return [0.0] * len(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    result = []
    for num in numbers:
        scaled_num = (num - min_val) / range_val
        result.append(scaled_num)
    return result