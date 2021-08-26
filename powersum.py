# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k) or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def power(a, b):        #5,2#5,1#5,0
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)    #5*power(5,1)#5*power(5,0)


def powerSum(n, k):#5,2
    # Your code goes here...
    if    n<0    or  k<0:
        return  0
    else:
        l=0
        l=power(n,k)
        return  l+powerSum(n-1,k)#power(5,2)+power(4,2)

#print(powerSum(3,10))

# Write your own test cases here...
assert(powerSum(2,10) == 1025)
assert(powerSum(3,10) == 60074)
print ("All test cases passed...")
