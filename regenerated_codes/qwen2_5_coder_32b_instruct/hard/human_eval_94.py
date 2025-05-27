'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def skjkasdkd(numbers):
    """Given a list of integers, find the largest prime number in the list and return the sum of its digits.
    If the list contains no prime numbers, return 0."""
    largest_prime = None
    
    for number in numbers:
        if is_prime(number):
            if largest_prime is None or number > largest_prime:
                largest_prime = number
    
    if largest_prime is None:
        return 0
    
    # Calculate the sum of the digits of the largest prime number
    digit_sum = sum(int(digit) for digit in str(largest_prime))
    
    return digit_sum