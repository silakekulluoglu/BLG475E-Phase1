'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def find_closest_elements(numbers):
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")
    
    # Sort the numbers to make it easier to find the closest pair
    sorted_numbers = sorted(numbers)
    
    min_diff = float('inf')
    closest_pairs = []
    
    # Iterate through the sorted list to find the closest pairs
    for i in range(len(sorted_numbers) - 1):
        diff = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
            closest_pairs = [(sorted_numbers[i], sorted_numbers[i + 1])]
        elif diff == min_diff:
            closest_pairs.append((sorted_numbers[i], sorted_numbers[i + 1]))
    
    # If there is more than one closest pair, raise a ValueError
    if len(closest_pairs) > 1:
        raise ValueError("Ambiguity: More than one pair has the same smallest difference.")
    
    return closest_pairs[0]