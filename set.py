# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    # Your code goes here...
    # l=[]
    # while   len(l)<=k:
    #     for i   in  range(0,6):
    #         if  i==0:
    #             l.append({})
    #         else:
    #             l.append({i})
    # return  l
    n=5
    l=[]
    for i   in  range(1,n+1):
        l.append(str(i))
    string=l
    return  (print_powerset(string,k))

#print(limitedPowerSet(5,7))
def jelement(e):
    l=[]
    
    s=''.join(e)
    if  s=='':
        return  {}

    elif  len(s)>1:
        for i   in  str(s):
            l.append(int(i))
    else:
        l.append(int(s))

    return  set(l)

#Python program to find powerset
from itertools import combinations
def print_powerset(string,k):
    l=[]
    for i in range(0,len(string)+1):
        for element in combinations(string,i):
            if  len(l)<=k-1:
                l.append(jelement(element))
            else:
                break

    return  l

print(limitedPowerSet(5,7))
