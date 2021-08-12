# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)


def dicetoorderedhand(a, b, c):
	# your code goes here
	if (a<=b):
		if (b<=c):
			return int(str(c)+str(b)+str(a))
		elif (c>a):
			return int(str(b)+str(c)+str(a))
		else:
			return int(str(b)+str(a)+str(c))
	else:
		if (a<c):
			return int(str(c)+str(a)+str(b))
		elif (c>b):
			return int(str(a)+str(c)+str(b))
		elif a==c:
			return int(str(a)+str(c)+str(b))
		else:
			return int(str(a)+str(b)+str(c))
	
