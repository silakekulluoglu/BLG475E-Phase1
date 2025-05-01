'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def pluck(arr):
    if len(arr) == 0:
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    if evens == []:
        return []
    return [min(evens), arr.index(min(evens))]