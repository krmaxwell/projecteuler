#!/usr/bin/python

from eulerlib import *

max=10 
lcm=max

""" 
The following method uses prime factorization and isn't working. This is 
because we don't account for prime factors raised to a power, e.g. 8=2^3.
"""

for i in range(max-1,2,-1):
	# if the lcm candidate is already divisible, we're done with that one
	print "Examining ",i," for ",lcm
	if (lcm % i) != 0:
		factors=prime_factors(i)
		print "* Factors for",i,"are",factors # debug output, really
		for j in prime_factors(i):
			if (lcm % j != 0): # WRONG
				print "* Multiplying by ",j
				lcm *= j
	else:
		print i," is already a factor"
	
print "LCM is",lcm
