def digits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a positive integer.")
    digits_product = 1
    digits = list(str(abs(n)))
    for digit in digits:
        if int(digit) % 2 == 1:
            digits_product *= int(digit)
    return digits_product if digits_product else 0
