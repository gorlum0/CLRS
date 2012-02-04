#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
from random import randrange

def find_missing(A):
    n = len(A)
    y = (0+n) * (n+1) // 2
    
    for x in A:
        j = 0
        while x:
            y -= (x&1) << j
            x >>= 1
            j += 1    
    return y

if __name__ == '__main__':
    A = range(10)
    i = randrange(len(A))
    del A[i]
    
    print i, find_missing(A) 
