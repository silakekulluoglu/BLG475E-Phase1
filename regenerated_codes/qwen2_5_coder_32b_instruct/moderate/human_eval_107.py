'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def even_odd_palindrome(n):
    if not isinstance(n, int) or n < 1 or n > 1000:
        raise ValueError("Input must be a positive integer between 1 and 1000 (inclusive).")
    
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        str_i = str(i)
        if str_i == str_i[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)