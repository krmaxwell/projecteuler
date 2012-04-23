#!/usr/bin/python

import sys

n=0
a=1
b=2
print "Calcuating sum..."
while (b <= 4000000):
	print "a=",a," b=",b
	if (b % 2) == 0:
		n += b
	a,b = b,a+b
print "Sum is ",n
