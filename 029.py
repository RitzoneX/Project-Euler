
l = {}
for i in xrange(2,1010):
    for j in xrange(2,1010):
        n = i ** j
        if n not in l:
            l[n] = None

print len(l)