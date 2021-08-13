# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...
import numpy
def isLatinSquare(lst):
    # Your code goes here...
    val=[]
    for i in range(len(lst)):
        val.append(i+1)
    
    #print(val)

    for i in lst:
        if set(i)!=set(val):
            return False

    #print("second-stage")
    r=numpy.array(lst)
    r=r.transpose()
    #print(r)

    for i in list(r):
    #   print(set(i),set(val))
        if set(i)!=set(val):
            return False
    return True

lst=[[1,2],[2,1]]

#print(isLatinSquare(lst))

assert(isLatinSquare(lst)==True)

lst=[[1,2,3],[2,3,1],[3,1,2]]
assert(isLatinSquare(lst)==True)

lst=[[1,2,3],[2,3,1],[1,2,3]]
assert(isLatinSquare(lst)==False)
print("All test cases passed!..")

