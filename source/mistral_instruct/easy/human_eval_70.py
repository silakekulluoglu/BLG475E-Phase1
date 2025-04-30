def strange_sort_list(lst):
    sorted_lst = sorted(lst)
    result = []
    for i in range(len(sorted_lst)):
        result.append(sorted_lst[i * 2])
    return result