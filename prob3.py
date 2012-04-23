#!/usr/bin/python

import sys

def prime_factors(n):
    """ Return the prime factors of the given number. """
    factors = []
    lastresult = n

    # 1 is a special case
    if n == 1:
        return [1]

    while lastresult != 1:
        c = 2
        while lastresult % c != 0:
            c += 1
        factors.append(c)
        lastresult /= c

    return factors

print prime_factors(600851475143)