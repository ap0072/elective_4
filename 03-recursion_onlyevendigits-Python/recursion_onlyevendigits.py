# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.


def printNo1s(n,l=[]):
    if n!=0:
        r=n%10
        if(r%2==0):
            l.append(r)
        printNo1s(n//10,l)
    return    l[::-1]

# Driver code
#print(printNo1s(17))


def helper(l,s=0,p=0): 
    if    len(l)!=0:
        #print("hi",l,s,p)
        s=s+((l[-1])*(10**p))
        #print(s,l[0:-1])
        return    helper(l[0:-1],s,p+1)
    else:
        return s
        
# val=(fun_recursion_onlyevendigits([4,3]))
# print(val)

def fun_recursion_onlyevendigits(l):
    l=l+[[]]
    return  fun_recursion_onlyevendigits01(l[0:-1],l[-1])
def  fun_recursion_onlyevendigits01(l,e=[]):
    if    len(l)!=0:
        val=((l[0]))
        #print(val)
        r=printNo1s(val,[])
        # if    (printNo1s(val))==[]:
        #     e.append([])
        # else:
        f=(helper(r))
        e.append(f)
        l=l[1:]
        #print(f'l:{l},e:{e},r:{r}')
        return    fun_recursion_onlyevendigits01(l,e)
    else:
        return    e
# result1=(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))
# result2=(fun_recursion_onlyevendigits([5, 0 , 66, 82, 121]))
print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))
print(fun_recursion_onlyevendigits([5, 0 , 66, 82, 121]))