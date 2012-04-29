#!/usr/bin/python

from eulerlib import *

max=20 
lcm=1
factors={}

for i in range(max-1,1,-1):
    candidate_factors=prime_factors(i)
    print "* Factors for",i,"are: ",
    print_factors(candidate_factors)
    for j in candidate_factors:
        if (not j in factors) or (candidate_factors[j] > factors[j]):
	    factors[j]=candidate_factors[j]
	
print "Factors of LCM are",
print_factors(factors)
for f in factors:
    lcm = lcm * f ** factors[f]
print "LCM is",lcm
