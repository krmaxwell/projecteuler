#!/usr/bin/python

from eulerlib import *

c=[]
curmax=0
imax=0
for i in range (1,1000000): 		# don't actually need to go to 1m (even)
    n = collatz_chain(i)
    if curmax < n:
        curmax = n
        imax = i
    c.append(n)
print "Term",imax,"goes to",curmax
