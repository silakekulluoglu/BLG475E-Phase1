def max_fill(grid, capacity):
    import math
    well_len = len(grid)
    water_count = sum([sum(row) for row in grid])
    times = math.ceil(water_count / capacity)
    return (times if times * capacity >= water_count else times + 1)