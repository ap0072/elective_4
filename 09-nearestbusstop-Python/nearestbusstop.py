# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	i=0
	j=8
	if street==0:
		return 0
	flag=True
	while(flag):
		print(i,j)
		if i==street:
			return i
		if j==street:
			return j
		if i<street & street<j:
			l=street-i
			u=j-street
			if l<=u:
				return i
			else:
				return j
		i=j
		j=j+8
print(fun_nearestbusstop(4))
		
