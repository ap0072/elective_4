# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import	math

def nthpowerfulnumber(n):
	# Your code goes here

		l=[]
		num=1
		while(len(l)-1!=n):
			val=primeFactors(num)
			#print(num,val,"val_value")
			r=powerfulnumber(str(val),num)
			if	r==True:
				l.append(num)
			num=num+1
		#print(l)
		return	l[-1]

def powerfulnumber(n,a):
	ln=n.split(",")
	ln=ln[0:-1]
	#print(ln)
	l=[int(i)	for	i	in	ln]

	l=set(l)
	l=list(l)
	#print(l)
	for	i	in	l:
		if(((a)%(i**2))!=0):
			return	False

	return	True



# A function to print all prime factors of
def primeFactors(n):
	s=""
	# Print the number of two's that divide n
	while n % 2 == 0:
		s=s+str(2)+","
		n = n / 2
		
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
		
		# while i divides n , print i ad divide n
		while n % i== 0:
			s=s+str(i)+","
			n = n / i
			
	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		s=s+str(int(n))+","

	return	s	

