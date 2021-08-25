# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	
	l=prasanth(row+1)
	# print(l)
	try:
		if len(l[row])+1==col:
			return 0
		return	l[row][col]
	except:
		# print("s")
		return None



def prasanth(n):
	l=[]
	m=[]
	for i in range(n):
		s=(i+1)*str(1)
		for j in s:
			m.append(int(j))
		l.append(m)
		m=[]
	

	for i in range(2,len(l)):
		for j in range(len(l[i])):
			if j!=0 and j!=len(l[i])-1:
				l[i][j]=(l[i-1][j])+(l[i-1][j-1])
	
	return	(l)


#print(prasanth(6))
print(fun_pascaltrianglevalue(2,1))
