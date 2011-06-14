#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

def binary_search(A, v):
    p, r = 0, len(A) - 1
    q = 0

    while v != A[q] and p <= r:
        q = (p + r) // 2
        if v < A[q]:
            r = q - 1
        else:
            p = q + 1

    return q if v == A[q] else -1

if __name__ == '__main__':
    A = [3, 3, 9, 26, 38, 41, 49, 52, 57, 57]

    print A
    v = 49
    print 'A[%d] = %d' % (binary_search(A, v), v)
