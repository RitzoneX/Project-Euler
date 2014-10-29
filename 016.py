power = 2 ** 1000
sum = 0
while power > 0:
    sum += power % 10
    power /= 10
print sum
