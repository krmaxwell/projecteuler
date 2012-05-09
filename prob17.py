#!/usr/bin/python

import sys

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
flag = False
numstr = ''

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

if not flag:
    hundred = n/100
    n = n % 100
    ten = n/10
    n = n % 10
    print hundred,' ',ten,' ',n
    if hundred > 1:
	print ones[hundred-1],"hundred and"
    if ten > 2:
	print tens[ten-1]
    print ones[n-1]
