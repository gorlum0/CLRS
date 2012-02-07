#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
import itertools as it
import collections as co
import random
from math import log, floor

def Random(a, b):
    def random_pow2(p):        
        r = 0
        for i in xrange(1, p+1):
            r = 2*r + random.randint(0, 1)
        return r

    p = int(2 ** floor(log(b-a, 2) + 1))
    while True:
        r = random_pow2(p)
        if r <= b-a:
            break
    return r+a

if __name__ == '__main__':
    print Random(1, 5)
    d = co.Counter(Random(1, 5) for _ in xrange(100))
    print 'd =', d
    print 'len(d) =', len(d)
