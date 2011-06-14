#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

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

        B.extend(A[i: q + 1])
        B.extend(A[j: r + 1])
        A[p: p + len(B)] = B

    if p < r:
        q = (p + r) / 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    A = [3, 41, 52, 26, 38, 57, 9, 49]

    print A
    merge_sort(A, 0, len(A)-1)
    print A
