'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def pluck(arr):
    if not arr or all(x % 2 != 0 for x in arr):
        return []

    evens = [x for x in arr if x % 2 == 0]
    idx, value = min((i, v) for i, v in enumerate(evens))
    return [value, idx]
