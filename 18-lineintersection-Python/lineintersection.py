# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	if (m1==m2) | (m2%m1==0) | (m1%m2==0):
		return None
	else:
		#y=mx+c
		#m1x1+c=m2x2+c -> m1-m2=b2-b1 
		v=(b2-b1)/(m1-m2)
		if v<0:
			v=v*-1
		return v
