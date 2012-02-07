#!/usr/bin/env python
"""(c) gorlum0 [at] gmail.com"""
import itertools as it
import collections as co
import random

def biased_random(p = 0.3):
    return 1 if random.random() <= p else 0

def unbiased_random():
    while True:
        x = biased_random()
        y = biased_random()
        if x != y:
            return x

if __name__ == '__main__':
    print unbiased_random()
    print co.Counter(unbiased_random() for _ in xrange(100))
