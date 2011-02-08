#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

def linear_search(A, v):
    for i in xrange(0, len(A)):
        if A[i] == v:
            return i
    return -1

def binary_search(A, v):
    p, r = 0, len(A) - 1
    q = 0

    while v != A[q] and p <= r:
        q = (p + r) / 2
        if v < A[q]:
            r = q - 1
        else:
            p = q + 1

    return q if v == A[q] else -1

if __name__ == '__main__':
    A = range(10); print A; print

    print linear_search(A, 5)
    print binary_search(A, 9)
