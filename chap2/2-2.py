#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
from sys import maxint as inf

def selection_sort(A):
    for i in xrange(len(A)-1):
        minv = inf
        minj = -1
        for j in xrange(i, len(A)):
            if A[j] < minv:
                minv = A[j]
                minj = j
        A[i], A[minj] = A[minj], A[i]

if __name__ == '__main__':
    A = [31, 41, 59, 26, 41, 58]

    print A
    selection_sort(A)
    print A
