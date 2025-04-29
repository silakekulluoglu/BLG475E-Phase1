def add(lst):
    if not lst:
        raise ValueError("The list should be non-empty.")

    return sum([val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0])