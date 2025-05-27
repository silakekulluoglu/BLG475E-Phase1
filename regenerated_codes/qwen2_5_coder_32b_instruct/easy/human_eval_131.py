'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def digits(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Convert the number to a string to iterate over each digit
    digits = str(n)
    
    # Initialize the product to 1 (neutral element for multiplication)
    product = 1
    
    # Flag to check if there are any odd digits
    has_odd_digit = False
    
    # Iterate over each character in the string representation of the number
    for char in digits:
        digit = int(char)
        if digit % 2 != 0:  # Check if the digit is odd
            product *= digit
            has_odd_digit = True
    
    # If no odd digits were found, return 0
    if not has_odd_digit:
        return 0
    
    return product