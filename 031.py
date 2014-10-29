
sum = 0
# for x in xrange(0,2):
# for y in xrange(0,3):
#     for z in xrange(0,5):
#         for i in xrange(0,11):
#             for j in xrange(0,41):
#                 for k in xrange(0,101):
#                     for l in xrange(0,201):
#                         if x * 200 + y * 100 + z * 50 +i * 20 + j * 5 + k * 2 + l == 200:
#                             sum += 1

for a in xrange(200, -1, -200):
    for b in xrange(a, -1, -100):
        for c in xrange(b, -1, -50):
            for d in xrange(c, -1, -20):
                for e in xrange(d, -1, -10):
                    for f in xrange(e, -1, -5):
                        for g in xrange(f, -1, -2):
                            sum += 1

print sum
