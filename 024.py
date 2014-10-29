digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
min_index = 0


def perm():
    global digits
    i = 1
    while not finish():
        if i == 1000000:
            break
        swap_index = swap()
        swap1 = digits[swap_index]
        digits[swap_index] = digits[min_index]
        digits[min_index] = swap1
        digits = digits[0:min_index + 1] + digits[-1:min_index:-1]
        i += 1
    print ''.join([str(x) for x in digits])


def finish():
    global min_index
    for i in xrange(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            min_index = i - 1
            return False
    return True


def swap():
    for i in xrange(len(digits) - 1, min_index, -1):
        if digits[i] > digits[min_index]:
            return i

perm()
# total = 1
# for x in xrange(len(digits), 0, -1):
#     total *= x
# print total