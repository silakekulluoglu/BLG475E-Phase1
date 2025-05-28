'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def pluck(arr):
    even_nodes = [i for i, value in enumerate(arr) if value % 2 == 0]
    if not even_nodes:
        return []

    smallest_even_value = min([arr[index] for index in even_nodes])
    smallest_even_index = next((index for index in even_nodes if arr[index] == smallest_even_value), None)
    return [smallest_even_value, smallest_even_index]