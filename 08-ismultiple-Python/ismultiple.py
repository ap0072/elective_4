# Write the function isMultiple that takes two int values m and n 
# and returns True if m is a multiple of n and False otherwise. 
# Note that 0 is a multiple of every integer including itself. 
# Also, you should make constructive use of the isFactor function you just wrote above.


def isFactor(m,n):
	if n<m:
		return False
	elif (n==0):
		return True
	elif (m%n==0):
		return True
	else:
		return False

def fun_ismultiple(m, n):
	return isFactor(m,n) # replace with your solution
