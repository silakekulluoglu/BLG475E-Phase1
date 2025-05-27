'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import math

def max_fill(grid, capacity):
    # Check if the grid is empty
    if not grid:
        raise ValueError("Grid cannot be empty.")
    
    # Check if each row is non-empty and all rows have the same length
    row_length = len(grid[0])
    if row_length == 0:
        raise ValueError("Each row must be non-empty.")
    
    for row in grid:
        if len(row) != row_length:
            raise ValueError("All rows must have the same length.")
    
    # Check if the grid exceeds 50 rows or 50 columns
    if len(grid) > 50 or row_length > 50:
        raise ValueError("Grid dimensions cannot exceed 50x50.")
    
    # Check if the bucket capacity is within the range 1 to 10
    if capacity < 1 or capacity > 10:
        raise ValueError("Bucket capacity must be between 1 and 10 inclusive.")
    
    # Check if all elements in the grid are either 0 or 1
    for row in grid:
        for cell in row:
            if cell not in (0, 1):
                raise ValueError("Grid can only contain 0s and 1s.")
    
    total_operations = 0
    
    for row in grid:
        water_units = sum(row)
        # Calculate the number of bucket operations needed using ceiling division
        operations = math.ceil(water_units / capacity)
        total_operations += operations
    
    return total_operations