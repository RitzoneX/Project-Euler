import object

def digit(n):
    m = 1
    for x in xrange(1, n + 1):
        m *= x
    return m

n = digit(100)
sum = 0
while n > 0:
	sum += n % 10
	n /= 10
print sum