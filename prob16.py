#!/usr/bin/python

import sys

if len(sys.argv) == 1:
    print "Define an exponent"
else:
    n = int(sys.argv[1])
    num = 2**n
    numstr = str(num)
    print "2 to",n,"is",numstr
    sum=0
    for i in range(0,len(numstr)):
	sum += int(numstr[i])
    print "Sum of digits in",numstr,"is",sum
