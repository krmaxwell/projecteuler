#!/usr/bin/python

import sys

def f(x,y):
    if x == 1 and y == 1:
	return 2
    elif x == 1:
	return 1 + f(x,y-1)
    elif y == 1:
	return 1 + f(x-1,y)
    else:
	return f(x-1,y) + f(x,y-1)

x=1
y=1
if len(sys.argv) == 3:
    x = int(sys.argv[1])
    y = int(sys.argv[2])

print "Size of",x,"x",y," is",f(x,y)
