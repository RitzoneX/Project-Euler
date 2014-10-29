
def reciprocal(n):
    m = {}
    a = 1
    i = 0
    while True:
        m[a] = i
        a = 10 * a % n
        i += 1
        if a in m:
            return i - m[a]

max = 0
num = 0
for x in xrange(1, 1000):
    cycle = reciprocal(x)
    if max < cycle:
        max = cycle
        num = x
print num, max