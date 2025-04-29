from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:

    if len(numbers) < 2:
        raise ValueError("Number of numbers should be at least two.")

    min_diff = float('inf')
    closest1 = closest2 = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest1 = numbers[i]
                closest2 = numbers[j]

    return (closest1, closest2)