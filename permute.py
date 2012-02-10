#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
import random

def permute_by_sorting(A):
    """O(n*lg(n))"""
    n = len(A)
    P = [0]*n
    for i in xrange(n):
        P[i] = random.randint(1, n**3)
    A.sort(key=lambda k: P[k])

def permute_in_place(A):
    """O(n)"""
    n = len(A)
    for i in xrange(n):
        j = random.randint(i, n-1)
        A[i], A[j] = A[j], A[i]

if __name__ == '__main__':
    A = range(10); print A
    permute_by_sorting(A); print A
    print

    A = range(10); print A
    permute_in_place(A); print A
