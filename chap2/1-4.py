#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""

def binary_sum(A, B):
    n = max(len(A), len(B))
    A = [0]*(n-len(A)) + A
    B = [0]*(n-len(B)) + B

    C = [0]*n; p = 0
    for i in xrange(n-1, -1, -1):
        p, C[i] = divmod(A[i] + B[i] + p, 2)
    if p: C = [p] + C

    return C

if __name__ == '__main__':
    A = [1, 1, 0, 0, 1]
    B = [1, 1, 0, 0, 1]
    n = max(len(A), len(B))
    fmt = '%%%ds' % len(str([0]*(n+1)))

    print fmt % A
    print fmt % '+'
    print fmt % B
    print fmt % '='
    print fmt % binary_sum(A, B)
