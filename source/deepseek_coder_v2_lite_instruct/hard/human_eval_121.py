'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])
