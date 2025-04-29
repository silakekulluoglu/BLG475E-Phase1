def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    avg = round(summation / (m - n + 1))
    return bin(avg)[2:]
