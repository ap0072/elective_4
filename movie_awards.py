# Write the function movieAwards(oscarResults) that takes a set of tuples, where each tuple holds the name of a category and the name of the winning movie, then returns a dictionary mapping each movie to the number of the awards that it won. For example, if we provide the set:
# { 
#     ("Best Picture", "The Shape of Water"), 
#     ("Best Actor", "Darkest Hour"),
#     ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
#     ("Best Director", "The Shape of Water"),
#     ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
#     ("Best Supporting Actress", "I, Tonya"),
#     ("Best Original Score", "The Shape of Water")
# }
# the function should return as follows
# { 
#     "Darkest Hour" : 1,
#     "Three Billboards Outside Ebbing, Missouri" : 2,
#     "The Shape of Water" : 3,
#     "I, Tonya" : 1
# }
oscarResults={ 
    ("Best Picture", "The Shape of Water"), 
    ("Best Actor", "Darkest Hour"),
    ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
    ("Best Director", "The Shape of Water"),
    ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
    ("Best Supporting Actress", "I, Tonya"),
    ("Best Original Score", "The Shape of Water")
}
def movieAwards(o):
    # Your code goes here...
    d=[]
    r={}
    for i in o:
        l=list(i)
        d.append(l[1])
    for i in d:
        if i in r.keys():
            r[i]=r[i]+1
        else:
            r[i]=1
    return r


print(movieAwards(oscarResults))