# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row. 
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the 
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6) 
# returns 3. Note that if any balls must be in a row, then you count that row, and so 
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).

def fun_numberofpoolballrows(balls):
	if balls==0:
		return 0
	k=1
	l=[]
	l2=[]
	l3=[]
	for i in range(1,balls+1):
		l.append(i)
	

	while(k<=balls):
		try:
			if k>len(l):
				for z in range(len(l)):
					l2.append(l[z])
			else:	
				for z in range(k):
					l2.append(l[z])
		except:
			pass
		l3.append(l2)
		l2=[]
		l=l[k:]
		k=k+1
	fl=0
	for i in l3:
		if len(i)!=0:
			fl=fl+1
	return fl

print(fun_numberofpoolballrows(4999950000))