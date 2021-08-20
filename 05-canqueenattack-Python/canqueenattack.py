# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.






def	validcoordinates(r,c):
	if	(r<1)	|	(r>8):
		return	False
	elif	(c<1)	|	(c>8):
		return	False
	else:
		return	True


def	leftdiagonal(r,c):
	l=[]
	r1=c
	c1=r
	while(validcoordinates(r1,c1)):
		#print(r1,c1)
		l.append([r1,c1])
		l.append([c1,r1])
		r1=r1-1
		c1=c1+1
		
	duplicates=l
	temp=[]
	for	i	in	duplicates:
		if	i	not	in	temp:
			temp.append(i)
	return	(temp)

#print(leftdiagonal(1,8))

def	rightdiagonal(r,c):
	l=[]
	r1=r
	c1=c
	while(validcoordinates(r1,c1)):
		#print("first-loop",r1,c1)
		l.append([r1,c1])
		r1=r1+1
		c1=c1+1
		
	
	while(validcoordinates(r,c)):
		#print("second-loop",r,c)
		l.append([r,c])
		r=r-1
		c=c-1
		

	#print(l)
	duplicates=l
	temp=[]
	for	i	in	duplicates:
		if	i	not	in	temp:
			temp.append(i)
	return	(temp)

#print(rightdiagonal(4,5))

def canqueenattack(qR, qC, oR, oC):
	if	(validcoordinates(qR,qC))	&	(validcoordinates(oR,oC)):
		#print("valid-coordinates")
		if	qR==oR:
			return	True
		else:
			if	qC==oC:
				return	True

			else:
				l=leftdiagonal(qR,qC)
				if	[oR,oC]	in	l:
					return	True
				else:
					l=rightdiagonal(qR,qC)
					if	[oR,oC]	in	l:
						return	True
					
					return	False

print(canqueenattack(4,5,6,7))
