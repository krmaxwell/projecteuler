#!/usr/bin/python

from eulerlib import *

i = 2
trinum = 1
divs=1
while divs <= 500:
    trinum = trinum+i
    divs = count_divisors(trinum)
    print i,"th triangle number",trinum,"has",divs,"divisors."
    i += 1

