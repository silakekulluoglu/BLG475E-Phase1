'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def strange_sort_list(lst):
    if not lst:
        return []

    results_list = []
    min_val = min(lst)
    results_list.append(min_val)
    lst.remove(min_val)

    while lst:
        max_val = max(lst)
        results_list.append(max_val)
        lst.remove(max_val)

        min_val = min(lst)
        results_list.append(min_val)
        lst.remove(min_val)

    return results_list
