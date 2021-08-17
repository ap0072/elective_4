# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.
import	numpy
def ismostlymagicsquare(a):
	# Your code goes here
	if	(len(a)==1)&(len(a[0])==1):
		return	True
	else:
		r=0
		c=0
		ld=0
		rd=0
		t=0
		for	i	in	a[0]:
			t=t+i

		for	i	in	a:
			for	j	in	i:
				r=r+j
			if	r!=t:
				return	False
			r=0

		n=numpy.array(a)
		n=list(n.transpose())
		for	i	in	n:
			for	j	in	i:
				c=c+j
			if	c!=t:
				return	False
			c=0

		p1=0
		p2=0
		for	i	in	range(len(a)):
			ld=ld+a[i][i]

		q2=len(a)-1
		for	i	in	range(len(a)):
			rd=rd+a[i][q2]
			q2=q2-1

		if	(t==ld)	&	(ld==rd):
			return	True
		else:
			return	False

#print(ismostlymagicsquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
