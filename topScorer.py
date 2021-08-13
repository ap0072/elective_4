# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    # Your code goes here...
    if len(data)==0:
        return None
    else:
        sl=data.splitlines()
        d=[]
        for i in sl:
            #print(i)
            d.append(i.split(","))
        #print(d)
        r={}
        for i in d:
            r[i[0]]=0
            t=0
            for j in i[1:]:
                j=int(j)
                t=t+j
            r[i[0]]=t
        m=0
        fl=[]
        #print(fl)
        for i in r.keys():
            fl.append(i)
            
        #print(r,type(r),fl,type(fl))
        if r[fl[0]]>r[fl[1]]:
            return (fl[0])
        elif r[fl[0]]==r[fl[1]]:
            return str(fl[0])+","+str(fl[1])
        else:
            return (fl[1])

data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
#print(topScorer(data))
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
