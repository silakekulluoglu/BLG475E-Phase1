from math import ceil

def rounded_avg(n, m):
    if not isinstance(n, int) or not isinstance(m, int):
        raise ValueError("Both n and m must be integers.")
    if n > m:
        return -1
    average = sum(range(int(n), int(m) + 1) / (m - n + 1))
    binary = bin(int(average))[2:]
    return binary.zfill(ceil(len(binary) + 1) + 1, '0')