def fact(n):
    result = 1
    for x in xrange(1, n + 1):
        result *= x
    return result
print fact(40)/fact(20)/fact(20)