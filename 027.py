
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

max = 0
for a in xrange(-1000, 1000):
    for b in xrange(1, 1000):
        n = 0
        while True:
            s = n * n + a * n + b
            if is_prime(s):
                n += 1
            else:
                break
        if n > max:
            max = n
            print a * b

