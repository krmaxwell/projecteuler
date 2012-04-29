#!/usr/bin/python

from eulerlib import *

n = 100
s1=sum_squares(n)
s2=square_sum(n)

print "Sum of squares of",n,"is",s1
print "Square of sum of ",n,"is",s2
print "Difference of sums is",s2-s1
