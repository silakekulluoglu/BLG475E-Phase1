def strange_sort_list(lst):
    if not lst:
        return []

    sorted_lst = []
    current_min = min(lst)
    current_max = max(lst)
    sorted_lst.append(current_min)
    while len(sorted_lst) < len(lst):
        for i in range(len(lst)):
            if lst[i] == current_min:
                continue
            elif lst[i] > current_max:
                current_max = lst[i]
            else:
                current_min = min([el for el in lst if el != current_min and el != 
current_max])
        sorted_lst.append(current_max)
        current_max = max(sorted_lst)
    return sorted_lst