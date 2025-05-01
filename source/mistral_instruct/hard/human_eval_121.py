'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def solution(lst):
    result = 0
    for i, num in enumerate(lst):
        if num % 2 != 0 and i % 2 == 0:
            result += num
    return result