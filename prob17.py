#!/usr/bin/python

import sys

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
flag = False
numstr = ''
i = 0

'''
if len(sys.argv) == 1:
    print "Give me a number"
    flag = True
else:
    n = int(sys.argv[1])
    if n >= 1000:
	print "Number should be under 1000"
	flag = True
    if n <= 0:
	print "Number should be positive"
        flag = True
'''

for n in range(1,1001):
    #numstr = ''
    hundred = n/100
    n = n % 100
    ten = n/10
    if n >= 20:
        n = n % 10

    #print hundred,' ',ten,' ',n		# debug code, to be removed
    if hundred == 10:
	numstr += 'onethousand'
    elif hundred > 0:
	numstr += ones[hundred-1]
	if ten == 0 and n == 0:
	    numstr += 'hundred'
	else:
	    numstr += 'hundredand'

    if ten > 1:
	numstr += tens[ten-1]
    if n != 0:
	numstr += ones[n-1]
    #numstr = ''.join(hundredstr, tens[ten-1], ones[n-1])
    #numstr = ''.join(['i' for i in xrange(numstr)])
    #print numstr

print len(numstr),'chars'

