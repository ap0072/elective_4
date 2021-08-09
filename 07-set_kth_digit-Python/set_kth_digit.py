# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
		if n<0:
			flag=True
		else:
			flag=False

		n1=str(n)
		fresh=[]
		for i in range(len(n1)): #i=0
			fresh.append(n1[i])
		fresh=fresh[::-1]
		if k==len(fresh):
			fresh.append(d)
		else:
			fresh[k]=d
		fresh=fresh[::-1]
		l=""
		for i in fresh:
			l=l+str(i)
		if flag:
			l=-1*int(l)
			return l
		else:
			return int(l)

# print(fun_set_kth_digit(468, 0, 1))