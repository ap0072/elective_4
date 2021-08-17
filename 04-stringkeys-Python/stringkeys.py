"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        val=self.calculate_hash_value(string)
        self.table[val]=string
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        val=self.calculate_hash_value(string)
        if (self.table[val]==string):
            return val
        else:
            return -1

    def calculate_hash_value(self, string1):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        return (ord(string1[0])*100+(ord(string1[1])))

# o=HashTable()
# print(o.calculate_hash_value("UDACIOUS"))
# print(o.lookup("UDACIOUS"))


