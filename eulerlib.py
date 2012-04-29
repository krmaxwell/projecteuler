# Frequently-used routines for Project Euler

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
    strn=str(n)
    return (strn == strn[::-1])

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
    sum=0
    for i in range(1,n+1):
	sum += i**2
    return sum

def square_sum(n):
    sum=0
    for i in range(1,n+1):
	sum += i
    return sum**2
