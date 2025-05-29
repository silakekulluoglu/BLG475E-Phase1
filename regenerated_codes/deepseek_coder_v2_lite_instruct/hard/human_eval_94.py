'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def skjkasdkd(lst):
    maxx = 0
    for num in lst:
        if num > maxx and isPrime(num):
            maxx = num
    result = sum(int(digit) for digit in str(maxx))
    return result
