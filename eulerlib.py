# Frequently-used routines for Project Euler
from math import *


def prime_factors(n):
    """ Return the prime factors of the given number. """
    factors = {}
    lastresult = n

    # 1 is a special case
    if n == 1:
        return {1: 1}

    while lastresult != 1:
        c = 2
        while lastresult % c != 0:
            c += 1
    if c in factors:
        factors[c] += 1
    else:
        factors[c] = 1
        lastresult /= c

    return factors


def is_palindrome(n):
    """ Return a value indicating whether a number is a palindrome."""
    return (str(n) == str(n)[::-1])


def print_factors(factors):
    first = True
    for n in factors:
        if not first:
            print "*",
        print n,
        if factors[n] != 1:
            print "^",
            print factors[n],
        first = False
    print


def sum_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum


def square_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum**2


def is_prime(n):
    r = trunc(sqrt(n))   # max number we have to check
    i = 2                # first number to check
    p = True             # eventual return value

    while (i <= r) and p:
        if (n % i) == 0:
            p = False
        else:
            i += 1       # skip even numbers
    return p


def prime_n(n):
    candidate = 2
    num = 1

    while num < n+1:
        if is_prime(candidate):
            num += 1
            candidate += 1
        else:
            candidate += 1
    return candidate-1


def count_divisors(n):
    divs = 0
    r = sqrt(n)
    for i in range(1, int(r)):
        if (n % i == 0):
            divs += 1
    divs = divs * 2
    if r.is_integer():
        divs -= 1
    return divs


def collatz_chain(n):
    i = 1

    while n != 1:
        if ((n >> 1) << 1) == n:
            n = n/2
        else:
            n = 3*n + 1
        i += 1
    return i
