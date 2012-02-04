#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
from __future__ import division

def parent(i): return i//2

def left(i): return 2*i

def right(i): return 2*i + 1

def heap_size(A): return len(A) - 1

def heapify(A, i):
    l, r = left(i), right(i)
    if l <= heap_size(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest)

def heapify2(A, i):
    """iter version"""
    while i <= heap_size(A)//2:
        l, r = left(i), right(i)
        if l <= heap_size(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r <= heap_size(A) and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
        i = largest

def build_heap(A):
    """1-based max-heap"""
    for i in xrange(heap_size(A)//2, 0, -1):
        heapify(A, i)

if __name__ == '__main__':
    A = [0, 5, 3, 17, 10, 84, 19, 6, 22, 9]
    print A
    build_heap(A)
    print A
