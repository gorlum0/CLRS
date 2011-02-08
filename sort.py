#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
from sys import maxint as inf

def insertion_sort(A):
    """noninc order"""
    for j in xrange(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

def selection_sort(A):
    B = [0] * len(A)

    for i in xrange(len(A)):
        minv = inf
        minj = -1
        for j in xrange(len(A)):
            if A[j] < minv:
                minv = A[j]
                minj = j
        B[i] = minv
        A[minj] = inf

    for i in xrange(len(A)):
        A[i] = B[i]

def merge_sort(A, p, r):
    """reserved"""
    def merge(A, p, q, r):
        B = []
        i, j = p, q + 1
        while i <= q and j <= r:
            if A[i] <= A[j]:
                B.append(A[i])
                i += 1
            else:
                B.append(A[j])
                j += 1

        while i <= q:
            B.append(A[i])
            i += 1
        while j <= r:
            B.append(A[j])
            j += 1

        for k in xrange(len(B)):
            A[k + p] = B[k]

    if p < r:
        q = (p + r) / 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    A0 = [10, 1, 5, 7, 88, -75]
    print A0; print

    A = A0[:]; insertion_sort(A); print A
    A = A0[:]; selection_sort(A); print A
    A = A0[:]; merge_sort(A, 0, len(A)-1); print A
