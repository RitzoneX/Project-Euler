import math


def count():
    result = 0
    for x in xrange(1, int(math.sqrt(sum)) + 1):
        if sum % x == 0:
            result += 2
            if sum / x == x:
                result -= 1
    return result

n = 1
sum = 0
while True:
    sum += n
    print n, sum, count()
    if count() > 500:
        break
    n += 1
