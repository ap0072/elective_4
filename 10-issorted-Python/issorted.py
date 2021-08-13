# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	if len(a)<=1:
		return True
	if a[0]>a[1]:
		flag="greater"
	else:
		flag="smaller"

	if flag=="greater":
		t=1
		i=0
		while(t!=len(a)):
			if (a[i+1]>a[i]):
				return False
			i=i+1
			t=t+1
		return True
	else:
		t=1
		i=0
		while(t!=len(a)):
			if (a[i+1]<a[i]):
				return False
			i=i+1
			t=t+1
		return True




print(issorted([1,1]))