def pluck(arr):
    if len(arr) == 0:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []
    smallest_even = min(evens)
    index = arr.index(smallest_even)
    return [smallest_even, index]
