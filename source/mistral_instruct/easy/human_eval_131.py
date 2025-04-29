def digits(n):
    if n < 10 or not n:
        return 0

    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0 and digit != 0:
            product *= digit
        n //= 10
    return product
