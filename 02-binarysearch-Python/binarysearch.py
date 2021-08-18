"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    l=input_array
    m=len(l)//2
    if  l[m]==value:
        return  m
    elif  value<l[m]:
        for i   in  range(m+1):
            if  l[i]==value:
                return  i
    else:
        for i   in  range(m+1,len(l)):
            if  l[i]==value:
                return  i
    return  -1
