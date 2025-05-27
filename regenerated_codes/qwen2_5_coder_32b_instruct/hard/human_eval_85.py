'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])