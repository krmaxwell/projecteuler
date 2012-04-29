#!/usr/bin/python

import sys
from eulerlib import *

# All the work is done by the module
n= 600851475143
factors = prime_factors(n)
print n," factors into:"
print_factors(factors)
