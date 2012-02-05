#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
import itertools as it
import numpy as np

def is_monge(A):
    m, n = A.shape
    X, Y = xrange(m), xrange(n)

    for x1,y1, x2,y2 in it.product(X, Y, X, Y):
        if x1 >= x2 or y1 >= y2:
            continue
        if A[x1,y1] + A[x2,y2] > A[x1,y2] + A[x2,y1]:
            print '--problem: x1,y1 = %d,%d; x2,y2 = %d,%d' % (x1,y1, x2,y2)
            return False
    return True

if __name__ == '__main__':
    A = np.mat('''
        10 17 13 28 23;
        17 22 16 29 23;
        24 28 22 34 24;
        11 13  6 17  7;
        45 44 32 37 23;
        36 33 19 21  6;
        75 66 51 53 34
    ''')

    print A
    print 'is_monge(A) =', is_monge(A)
    print

    B = np.mat('''
        37 23 22 32;
        21  6  7 10;
        53 34 30 31;
        32 13  9  6;
        43 21 15  8
    ''')

    print B
    x = is_monge(B)
    print 'is_monge(B) =', x
    B[1,2] = 2
    print B
    print 'is_monge(B) =', is_monge(B)
