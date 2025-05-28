'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def fizz_buzz(n: int):
    count = 0
    for num in range(1, n):
        if (num % 11 == 0 or num % 13 == 0) and '7' in str(num):
            count += sum([1 for digit in str(num) if digit == '7'])
    return count