'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def skjkasdkd(lst):
    # Find the largest prime number in lst
    primes = [2]
    for num in lst:
        if all(num % i != 0 for i in primes):
            primes.append(num)

    # Determine the sum of the digits of the largest prime number
    largest_prime = max(primes)
    result = 0
    while largest_prime > 0:
        rem = largest_prime % 10
        result += rem
        largest_prime //= 10
    return result