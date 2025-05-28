'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def sorted_list_sum(lst):
    lst = [num for num in lst if len(num) % 2 == 0]
    lst.sort(key=lambda s: (len(s), s))
    return lst