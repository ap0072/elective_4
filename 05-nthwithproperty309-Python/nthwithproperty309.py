# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def property309(n):
	# Your code goes here
	n=n**5
	s=str(n)
	for	i	in	range(10):
		if	str(i)	not	in	s:
			return	False
	return	True
def	nthwithproperty309(n):
	l=[]
	i=0
	while(len(l)<n+1):
		if	property309(i):
			l.append(i)
		i=i+1
	return	l[-1]
print(nthwithproperty309(1))
