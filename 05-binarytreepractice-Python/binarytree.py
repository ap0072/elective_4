class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def search(self, find_val):
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        if  find_val==None:
            return  False
        
        else:
            temp1=self.root
            temp2=self.root
            try:
                while(temp1):
                    if  temp1.value==find_val:
                        return  True
                    elif    temp2.value==find_val:
                        return  True
                    else:
                        temp1=temp1.left
                        temp2=temp2.right
            except:
                pass

            return  False

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        temp1=self.root
        temp2=self.root
        try:
            while(temp1):
                print(temp1.value)
                print(temp2.value)
                temp1=temp1.left
                temp2=temp2.right
        except:
            pass


    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        if  find_val==None:
            return  False
        
        else:
            temp1=self.root
            temp2=self.root
            try:
                while(temp1):
                    if  temp1.value==find_val:
                        return  True
                    elif    temp2.value==find_val:
                        return  True
                    else:
                        temp1=temp1.left
                        temp2=temp2.right
            except:
                pass

            return  False

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        temp1=self.root
        temp2=self.root
        try:
            while(temp1):
                print(temp1.value)
                print(temp2.value)
                temp1=temp1.left
                temp2=temp2.right
        except:
            pass

tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
#tree.print_tree()
print(tree.search("4"))