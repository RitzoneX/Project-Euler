

def fun(n):
    sum = 0
    while n > 0:
        sum += (n % 10) ** 5
        n /= 10
    return sum

sum = 0
for x in xrange(2,1000000):
    if x == fun(x):
        sum += x
print sum
