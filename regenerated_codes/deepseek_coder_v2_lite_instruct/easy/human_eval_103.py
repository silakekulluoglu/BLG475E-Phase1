'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def rounded_avg(n, m):
    if n > m:
        return -1
    total = sum(range(n, m + 1))
    avg = round(total / (m - n + 1))
    return bin(avg)