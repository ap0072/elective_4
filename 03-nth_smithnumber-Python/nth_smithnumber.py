# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math
 
# A function to print all prime factors of
# a given number n
def primeFactors(n):
    l=[] 
    # Print the number of two's that divide n
    while n % 2 == 0:
        l.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            l.append(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        l.append(int(n))
    return  l

def smithnumber(n):
    l=primeFactors(n)
    if  len(l)<2:
        return  False
    else:

        nsum=0
        for i   in  str(n):
            nsum=nsum+int(i)


        r=0
        for i   in  l:
            if  len(str(i))>1:
                s=0
                for j  in   str(i):
                    s=s+int(j)
                r=r+s
            else:
                r=r+i
        resultsum=r

        if  (resultsum==nsum):
            return  True
        else:
            return  False
 
#print(smithnumber(0))

def fun_nth_smithnumber(n):
    n1=n+1
    l=[]
    i=4
    while(len(l)<n1):
        if(smithnumber(i)):
            l.append(i)
        i=i+1
    return  l[-1]
#print(fun_nth_smithnumber(0))


