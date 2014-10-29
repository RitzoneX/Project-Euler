import math


# def fib(n):
#     a = 0
#     b = 1
#     for x in xrange(n):
#         a, b = b, a + b
#     return a

# i = 1
# while math.log10(fib(i)) < 999:
#     i += 1
# print i

a = 1
b = 1
i = 1
while math.log10(a) < 999:
    a, b = b, a + b
    i += 1
print i