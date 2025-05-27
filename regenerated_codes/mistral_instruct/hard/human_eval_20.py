'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

from typing import List, Tuple
import math

EPSILON = 1e-9

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("The given list must have at least two elements.")

    min_diff = float('inf')
    closest1 = None
    closest2 = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(math.fabs(numbers[i]) - math.fabs(numbers[j]))
            if diff < min_diff - EPSILON:
                closest1, closest2 = numbers[i], numbers[j]
                min_diff = diff
    if closest1 > closest2:
        closest1, closest2 = closest2, closest1
    return (closest1, closest2)