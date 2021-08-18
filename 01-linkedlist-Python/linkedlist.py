"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        #print(self.head.value)

        if  self.head==None:
            self.head=new_element
        else:
            temp=self.head
            temp1=self.head.next
            while(temp1!=None):
                temp1=temp1.next
                temp=temp.next
            p=temp.next
            temp.next=new_element
            new_element=p

            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        pos=1
        temp=self.head
        while  (temp):
            if  pos==position:
                return  temp
            else:
                temp=temp.next
                pos=pos+1
        return None
    
    def insert(self, new_element,position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        if  self.head==None:
            self.head=new_element
        else:
            #print("entered")
            pos=1
            temp=self.head
            while(temp):
                if(pos==position-1):
                    #print("got_u",pos,position-1)
                    p=temp.next
                    temp.next=new_element
                    new_element.next=p
                    break
                temp=temp.next
                pos=pos+1
    
    def allvalues(self):
        temp=self.head
        while  (temp):
            print(temp.value)
            temp=temp.next

    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp=self.head
        while  (temp!=None):
            if(temp.value)==value:
                if  (temp==self.head):
                    p=temp.next
                    self.head=p
                    break
                else:
                    if  (temp.next==None):
                        previous.next=None
                    else:
                        p=temp.next
                        previous.next=p
                break
            previous=temp
            temp=temp.next
            


# l=LinkedList(Element(1))
# l.append(Element(2))
# l.append(Element(3))
# l.insert(1,1)
# l.insert(2,2)
#l.allvalues()
#print(l.delete(1))

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList(e1)
# ll.append(e1)
ll.append(e2)
ll.append(e3)
# ll.allvalues()
#print(ll.get_position(3))
e4 = Element(4)
ll.insert(e4,3)
# ll.allvalues()
#print(ll.get_position(3))
ll.delete(1)
ll.allvalues()