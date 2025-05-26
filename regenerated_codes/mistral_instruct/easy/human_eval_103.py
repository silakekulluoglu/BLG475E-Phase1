'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def rounded_avg(n, m):
    if n > m:
        return -1

    average = int((sum(range(n, m + 1)) / (m - n + 1)))
    binary = format(average, '0b')
    return binary