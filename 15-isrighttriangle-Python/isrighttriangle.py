# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import  math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
	b=math.sqrt(((x1-x3)**2)+((y1-y3)**2))
	c=math.sqrt(((x2-x3)**2)+((y2-y3)**2))
	h=max(a,b,c)
	print(a,b,c)
	l=[a,b,c]
	m=[]
	for i in l:
		if i!=h:
			m.append(i)
	s=0	
	for i in m:
		s=s+i**2
	if s==h**2:
		return True
	else:
		return False

print(isrighttriangle(-1, 7, 10, -4, 12, -2))