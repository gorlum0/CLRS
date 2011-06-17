#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

def binary_search(A, v):
    lo, hi = 0, len(A) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if v == A[mid]:
            return mid
        elif v > A[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == '__main__':
    A = [3, 3, 9, 26, 38, 41, 49, 52, 57, 57]

    print A
    v = 49
    print 'A[%d] = %d' % (binary_search(A, v), v)
