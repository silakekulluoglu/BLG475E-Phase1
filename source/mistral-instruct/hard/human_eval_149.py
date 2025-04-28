def sorted_list_sum(lst):
    odd_length = [num for num in lst if len(num) % 2 != 0]
    filtered_list = [num for num in lst if len(num) % 2 == 0]

    # Sort the filtered list first by length, then alphabetically
    sorted_list = sorted(filtered_list, key=len)
    sorted_list.sort()

    return sorted_list + odd_length