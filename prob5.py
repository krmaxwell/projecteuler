#!/usr/bin/python

import sys

from eulerlib import *

if len(sys.argv) == 1:
    n = 10
else:
    n = sys.argv[1]

lcm=1
factors={}

for i in range(n-1, 1, -1):
    candidate_factors = prime_factors(i)
    print "* Factors for %d are: %s" % (i, print_factors(candidate_factors))
    for j in candidate_factors:
        if (not j in factors) or (candidate_factors[j] > factors[j]):
            factors[j] = candidate_factors[j]

print "Factors of LCM are %s" % print_factors(factors)
for f in factors:
    lcm = lcm * f ** factors[f]
print "LCM is %d" %lcm
