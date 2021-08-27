# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    x1=left1
    y1=top1
    w=width1
    h=height1
    l=[]
    bL=[x1,y1]      #bottom left
    bR=[x1+w,y1]    #bottom right
    tL=[x1,y1+h]    #top    left
    tR=[x1+w,y1+h]  #top    right
    l=l+[bL,bR,tL,tR]

    #print(l)

    x11=left2
    y11=top2
    w1=width2
    h1=height2
    m=[]
    bL1=[x11,y11]
    bR1=[x11+w,y11]
    tL1=[x11,y11+h1]
    tR1=[x11+w1,y11+h1]
    m=m+[bL1,bR1,tL1,tR1]
    #print(m)

    for i   in  range(len(l)):
        if  l[i]    in  m:
            return True
    return  False

        
print(fun_rectangle_overlap(0,2,1,4,1,6,8,4)) 
        
