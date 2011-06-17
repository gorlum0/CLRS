#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

def merge_sort(A, p, r):
    """merge-sort which counts inversions"""
    def merge(A, p, q, r):
        B = []
        i, j = p, q + 1
        inv = 0
        while i <= q and j <= r:
            if A[i] <= A[j]:
                B.append(A[i])
                i += 1
            else:
                B.append(A[j])
                inv += q - i + 1
                j += 1

        B.extend(A[i: q + 1])
        B.extend(A[j: r + 1])
        A[p: p + len(B)] = B

        return inv

    inv = 0
    if p < r:
        q = (p + r) // 2
        inv += merge_sort(A, p, q)
        inv += merge_sort(A, q + 1, r)
        inv += merge(A, p, q, r)

    return inv

if __name__ == '__main__':
    A = [2, 3, 8, 6, 1]

    print A
    print merge_sort(A, 0, len(A)-1)
    print A
