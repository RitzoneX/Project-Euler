from pprint import pprint

names = None
with open('p022_names.txt') as f:
    names = sorted(eval(f.read()))


def worth(name):
    sum = 0
    for x in name:
        sum += ord(x) - ord('A') + 1  # A = 1
    return sum

total = 0
for i in xrange(len(names)):
    total += (i + 1) * worth(names[i])

print total
