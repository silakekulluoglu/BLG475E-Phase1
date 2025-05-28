'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def truncate_number(num):
    if num <= 0 or num >= 1e16:
        raise ValueError("Input must be a positive floating-point number less than 1e16.")
    
    # Get the fractional part by subtracting the integer part from the number
    decimal_part = num - int(num)
    return decimal_part