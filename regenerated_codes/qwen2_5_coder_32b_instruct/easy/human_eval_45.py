'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def triangle_area(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    
    # Calculate the area using the formula (a * h) / 2
    area = (a * h) / 2
    
    return area