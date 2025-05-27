'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def pluck(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    
    smallest_even = None
    smallest_index = None
    
    for index, value in enumerate(numbers):
        if not isinstance(value, int) or value < 0:
            raise ValueError("All elements in the list must be non-negative integers.")
        
        if value % 2 == 0:  # Check if the number is even
            if smallest_even is None or value < smallest_even:
                smallest_even = value
                smallest_index = index
    
    if smallest_even is not None:
        return [smallest_even, smallest_index]
    else:
        return []