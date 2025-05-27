'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def rounded_avg(n, m):
    if n <= 0 or m <= 0:
        raise ValueError("Both n and m must be positive integers.")
    
    if n > m:
        return -1
    
    # Calculate the sum of integers from n to m (inclusive)
    total_sum = sum(range(n, m + 1))
    
    # Calculate the number of integers from n to m (inclusive)
    count = m - n + 1
    
    # Calculate the average
    average = total_sum / count
    
    # Round the average according to the specified rules
    rounded_average = int(average + 0.5)
    
    # Convert the rounded average to a binary string
    binary_result = bin(rounded_average)
    
    return binary_result