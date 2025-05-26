'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def rounded_avg(n, m):
    if n <= 0 or m <= 0:
        return -1
    if n > m:
        return -1

    total = sum(range(n, m + 1))  # Compute the sum of the integers from n through m (including n and m)
    avg = round(total / (m - n + 1))  # Round the average to the nearest integer and convert it to decimal
    binary_avg = bin(avg)[2:]  # Convert the decimal value to binary

    return f"0b{binary_avg.zfill(len(str(m - n + 1)))}"  # Add leading zeros if necessary so that the binary string has the same length as the number of integers from n through m
