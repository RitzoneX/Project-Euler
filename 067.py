from pprint import pprint

s = ''
with open('p067_triangle.txt') as f:
    s = f.read().strip()

l = [x.split() for x in s.split('\n')]
for i in xrange(len(l) - 1, 0, -1):
    for j in xrange(len(l[i - 1])):
        max = l[i][j] if l[i][j] > l[i][j + 1] else l[i][j + 1]
        l[i - 1][j] = int(l[i - 1][j]) + int(max)
pprint(l[0][0])
