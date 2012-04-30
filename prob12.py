#!/usr/bin/python

from eulerlib import *

i = 0
numdivs = 0
trinum = 1
while numdivs < 5:
    trinum = trinum+i
    print "Checking",i,"th triangle number ",trinum
    divs = list_divisors(trinum)
    numdivs = len(divs)
    i += 1

print "Triangle number",trinum,"has",numdivs,"divisors:"
print divs
