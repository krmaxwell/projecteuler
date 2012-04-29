#!/usr/bin/python

import sys
from eulerlib import *

# All the work is done by the module
n= 600851475143
factors = prime_factors(n)
print "Factoring",n,"into:"
first = True
for n in factors:
	if not first:
		print "*",
	print n,
	if factors[n] != 1:
		print "^",
		print factors[n],
	first = False
