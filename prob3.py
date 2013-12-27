from eulerlib import *

# All the work is done by the module
n = 600851475143
factors = prime_factors(n)
print "Largest prime factor of %d is %d" % (n, max(factors.keys()))
