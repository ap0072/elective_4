"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class stack(object):
    def __init__(self,top=None):
        self.head = Element(top)
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def push(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head==None:
            self.head=Element(new_element)
        else:
            k=Element(new_element)
            k.next=self.head
            self.head=k


    def pop(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head==None:
            return None
        else:
            k=self.head
            self.head=self.head.next
            k.next=None
            return k

# class stack(object):
#     def __init__(self,top=None):
#         self.ll = LinkedList(None)

#     def push(self, new_element):
#         "Push (add) a new element onto the top of the stack"
#         ll.insert_first(new_element)
#         pass

#     def pop(self):
#         "Pop (remove) the first element off the top of the stack and return it"
#         ll.delete_first()

#stack.push(Element(1))