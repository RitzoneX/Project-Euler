def SumOfDivisors(n):
    sum = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n / p
            while n % p == 0:
                j = j * p
                n = n / p
            sum = sum * (j - 1)
            sum = sum / (p - 1)
        if p == 2:
            p = 3
        else:
            p = p + 2
    if n > 1:
        sum = sum * (n + 1)
    return sum


def SumOfProperDivisors(n):
    return SumOfDivisors(n) - n

abundants = [x for x in xrange(1, 28124) if SumOfProperDivisors(x) > x]
d = {}
for x in abundants:
    d[x] = None
sum = 0
for n in xrange(28124):
    i = 0
    while i < len(abundants) and abundants[i] * 2 <= n:
        if n - abundants[i] in d:
            break
        i += 1
    else:
        sum += n
print sum

