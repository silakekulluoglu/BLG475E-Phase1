'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def even_odd_palindrome(n):
    evens = sum([1 for x in range(1, n) if str(x) == str(x)[::-1] and x % 2 == 0])
    odds = sum([1 for x in range(1, n) if str(x) == str(x)[::-1] and x % 2 != 0])

    return (evens, odds)