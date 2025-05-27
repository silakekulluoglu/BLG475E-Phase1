'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def solution(lst):
    if not lst or any(isinstance(num, (float, str)) for num in lst):
        raise TypeError("List must contain only integers")

    result = 0
    for i, num in enumerate(lst):
        if type(num) is float or isinstance(num, str):
            raise TypeError("List must contain only integers")
        if i % 2 == 0 and num % 2 != 0:
            result += num
    return result