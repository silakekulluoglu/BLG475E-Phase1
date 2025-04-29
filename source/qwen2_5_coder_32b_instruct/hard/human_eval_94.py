def skjkasdkd(lst):
    def isPrime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    maxx = 0
    for i in lst:
        if i > maxx and isPrime(i):
            maxx = i

    result = sum(int(digit) for digit in str(maxx))
    return result