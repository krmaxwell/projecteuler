#!/usr/bin/python

max=10 
lcm=max

def prime_factors(n):
    """ Return the prime factors of the given number. """
    factors = []
    lastresult = n

    # 1 is a special case
    if n == 1:
        return [1]

    while lastresult != 1:
        c = 2
        while lastresult % c != 0:
            c += 1
        factors.append(c)
        lastresult /= c

    return factors

for i in range(max-1,2,-1):
	# if the lcm candidate is already divisible, we're done with that one
	print "Examining ",i," for ",lcm
	if (lcm % i) != 0:
		for j in prime_factors(i):
			if (lcm % j != 0):
				print "  Multiplying by ",j
				lcm *= j
	else:
		print i," is already a factor"
	
print "LCM is",lcm
