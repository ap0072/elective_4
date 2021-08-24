# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the 
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2 
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the 
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use 
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some 
# helper functions that do part of the work, and then those helper functions will make our final 
# function much easier to write. 

# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will 
# be represented by the integer 432. With that, let's start writing some code. Be sure to write 
# your functions in the same order as given here, since later functions will make use of earlier 
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns 
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice 
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it 
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by 
# calling score, which you already wrote). The function should return two values -- the resulting hand 
# and the score for that hand. For example:
# (bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# (bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# (bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# (bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# (bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# (bonusPlayThreeDiceYahtzee(2333555) == (555, 35))

def	bonusPlayThreeDiceYahtzee(dice):	
	
	s=str(dice)[::-1]
	#print(f"*****{s}***")
	L=[]
	for	i	in	s:
		L.append(int(i))

	bonusPlayThreeDiceYahtzee1(L[0:3],True,0,L)

def bonusPlayThreeDiceYahtzee1(dice,flag,i,L):
	# Your code goes here
	# 
	i=i
	l,c,i=counter_val(dice,flag,i)

	if	c==0:
		print	(*l,"	",20+(3*l[0]))

	elif	c==1:
		if	i!=6:
			bonusPlayThreeDiceYahtzee1(l+L[i:],False,i,L)
		else:
			print(*l,"	",10+(2*l[0]))
	elif	c==2:
		if	i!=6:
			#print("Back-to-home",l+L[i:])
			bonusPlayThreeDiceYahtzee1(l+L[i:],False,i,L)

		else:
			print(*l,"	",max(l))



def	counter_val(l,flag,i):
	try:
		#print(f"Entered_into_counter_val	funcction	with{l}	and	ivalue	as	{i}")
		a=l[0]
		b=l[1]
		c=l[2]
		l=[]

		if	a==b	and	b==c:
			#print("All-val-is-common")
			counter=0
			l.append(int(a))
			l.append(int(b))
			l.append(int(c))
			return	l,counter,i

		elif	a==b	and	a!=c:
			#print("One-val-is-common")
			counter=1
			l.append(int(a))
			l.append(int(b))
			if	flag:
				i=i+3
			else:
				i=i+1

			if	i==6:
				return	[a,b,c],counter,i
			else:
				return	l,counter,i
		
		elif	a==c	and	a!=b:
			#print("One-val-is-common")
			counter=1
			l.append(int(a))
			l.append(int(c))
			if	flag:
				i=i+3
			else:
				i=i+2
			
			if	i==6:
				return	[a,b,c],counter,i
			else:
				return	l,counter,i
		


		elif	b==c	and	b!=a:
			#print("One-val-is-common")
			counter=1
			l.append(int(c))
			l.append(int(b))

			if	flag:
				i=i+3
			else:
				i=i+2
			
			if	i==6:
				return	[a,b,c],counter,i
			else:
				return	l,counter,i

		else:
			#print("No-val-is-common")
			counter=2
			m=max(int(a),int(b),int(c))
			l.append(m)

			if	flag:
				i=i+3
			else:
				i=i+2
			
			if	i==6:
				return	[a,b,c],counter,i
			else:
				return	l,counter,i

	except:
		return	(l,2,6)

#bonusPlayThreeDiceYahtzee(2345413)



(bonusPlayThreeDiceYahtzee(2312413) == ( 4))
(bonusPlayThreeDiceYahtzee(2315413) == (5))
(bonusPlayThreeDiceYahtzee(2345413) == (18))
(bonusPlayThreeDiceYahtzee(2633413) == (16))
(bonusPlayThreeDiceYahtzee(2333413) == (29))
(bonusPlayThreeDiceYahtzee(2333555) == (35))
