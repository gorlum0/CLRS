#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

def insertion_sort(A):
    """noninc order"""
    for j in xrange(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

if __name__ == '__main__':
    A = [31, 41, 59, 26, 41, 58]

    print A
    insertion_sort(A)
    print A
