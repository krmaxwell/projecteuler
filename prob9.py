#!/usr/bin/python

# Uses Euclid's algorithm
for n in range(1,1000):
    for m in range(n,1000):
	a = m**2 - n**2
	b = 2*m*n
	c = m**2+n**2
	if (a+b+c == 1000):
	    print "a=",a,", b=",b,", c=",c," product=",a*b*c
