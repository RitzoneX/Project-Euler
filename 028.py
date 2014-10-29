
step = 2
n = 1
sum = 1
while n < 1001 * 1001:
    for x in xrange(4):
        n += step
        sum += n
    step += 2

print sum