#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

def linear_search(A, v):
    for i in xrange(0, len(A)):
        if A[i] == v:
            return i
    return -1

if __name__ == '__main__':
    A = [31, 41, 59, 26, 41, 58]

    print A
    x = 59; y = linear_search(A, x)
    print 'A[%d] = %d' % (y, x)
