#!/usr/bin/python

from eulerlib import *

result=0
for i in range(100,1000):
	for j in range (100,1000):
		n=i*j
		if (is_palindrome(n)) and n>result:
			lasti = i
			lastj = j
			result = n
print result," is the product of ",lasti," and ",lastj
