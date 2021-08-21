# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

from math import floor

def	powerof3(n,e,i):

	if	i<=n:
		
		e.append(i)

		i=i*3
		return	powerof3(n,e,i)
	return	e



def recursion_powersof3ton(n):
	# Your code goes here
	n=floor(n)
	r=powerof3(n,[],1)
	if	len(r)==0:
		return	None
	
	return	r

print(recursion_powersof3ton(100))
