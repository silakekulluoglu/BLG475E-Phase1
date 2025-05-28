'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''
def even_odd_palindrome(n):
    # Check if n is positive integer
    if n <= 0:
        raise ValueError("Input must be a positive integer between 1 and 10^3")

    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even += 1
        elif str(i) == str(i)[::-1] and i % 2 != 0:
            odd += 1
    return even, odd