'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def strange_sort_list(lst):
    result = [min(lst)]
    while lst:
        if len(result) % 2 == 0:
            max_num = max(lst)
            index = lst.index(max_num)
            del lst[index]
        else:
            min_num = min(lst)
            index = lst.index(min_num)
            del lst[index]
        result.append(min(lst) if len(result) % 2 == 0 else max(lst))
    return result