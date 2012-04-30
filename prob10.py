#!/usr/bin/python

from eulerlib import *

mysum = 0

for n in range(2,2000000):
	if is_prime(n):
		mysum += n
print "Sum is",mysum
