#!/usr/bin/python

result=0
for i in range(100,1000):
	for j in range (100,1000):
		n=i*j
		strn=str(n)
		if (strn == strn[::-1]) and n>result:
			lasti = i
			lastj = j
			result = n
print result," is the product of ",lasti," and ",lastj
