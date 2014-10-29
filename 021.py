from pprint import pprint
import math


# def d(n):
#     if n == 1:
#         return 0
#     r = int(math.sqrt(n))
#     # //first take into account the case that n is a perfect square.
#     sum = 1
#     if r * r == n:
#         sum += r
#         r = r - 1
#     # if odd(n):
#     #     f = 3 step = 2 else f = 2 step = 1
#     f = 2
#     while f <= r:
#         if n % f == 0:
#             sum = sum + f + n / f
#         f = f + 1
#     return sum
# sum = 1
# for x in xrange(2, int(math.sqrt(n))):
#     if n % x == 0:
#         sum += x + n / x
#     if x * x == n:
#         sum -= x
# return sum


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

def d(n):
	return SumOfDivisors(n) - n

s = []
for a in xrange(1, 1000000):
    b = d(a)
    if a < b and d(b) == a:
        s.append(a)
        s.append(b)

print s
print sum(s)
