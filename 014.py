def collatz(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1


def count(num):
    n = 1
    while num != 1 and num not in d:
        num = collatz(num)
        n += 1
    return n + d.get(num, 0)

longest = 0
max = 0
d = dict()
for x in xrange(1, 1000000):
    d[x] = count(x)
    if longest < d[x]:
        longest = d[x]
        max = x

print max
