# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.

import math
def fun_distance(x1, y1, x2, y2):
	# your code goes here
	v=math.sqrt((x2-x1)**2+(y2-y1)**2)
	v=str(v)
	v1=v.split(".")
	return int(v1[0])
#print(fun_distance(30, 37, 79, -51))