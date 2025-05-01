'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def max_fill(grid, capacity):
    import math
    return sum([math.ceil(sum(arr) / capacity) for arr in grid])
