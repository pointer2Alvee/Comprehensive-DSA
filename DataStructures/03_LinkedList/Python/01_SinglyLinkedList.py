"""
© alvee 2024
email : pointer2alvee@gmail.com 

Comprehensive SLL Operations/Algorithms :
-----------------------------------------
(1) Create:
    (1.1) Node-Class
    (1.2) SLL-Class
(2) Insert Node
    (2.1) prepend() : Insert node in the beginning of SLL
    (2.2) insert()  : Insert node in any position of SLL
    (2.3) append()  : Insert node in the end of SLL
(3) traverse() : Traverse the SLL
(4) search() : Search for any Node in SLL
(5) get() : Get the node for a given index
(6) set() : Set the node data for a given index
(7) Remove Node:
    (7.1) pop_first() : Removes the first node of the SLL 
    (7.2) pop()       : Removes the last node of the SLL
    (7.3) remove()    : Removes any particular node in the SLL
    (7.4) delete()    : Deletes the entire SLL
"""

############### Singly Linked List (SLL) ###############
########################################################

# (1.1) Create Node :
class Node:
    def __init__(self,data) -> None:
        """
        Creates a single node of the SLL
        """
        self.data = data 
        self.next = None 
        
# (1.2) SLL Class
class SinglyLinkedList:
    
    # (1.2) Empty SLL Class
    def __init__(self) -> None:
        """
        Creates an empty SLL with no nodes
        """
        self.head = None
        self.tail = None
        self.length = 0
    
    
    # __str__() method moification for custom print 
    def __str__(self) -> str:
        """
        Modifys/overrides the inbuilt __str__() method for custom SLL printing format
        """
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.data)
            if temp_node.next is not None:
               result += "-->"
            temp_node = temp_node.next
        return result
    
    
    # (2.1) prepend() method
    def prepend(self, data):
        """
        Add a new node in the beginning of the SLL. Edge cases handled
        """
        new_node = Node(data)
        
        if self.head == None:
            self.head = self.tail = new_node  
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    
    # (2.3) append() method
    def append(self, data):
        """
        Adds a new Node in the end of the SLL. Edge cases handled
        """
            


################## SLL implementations #################
########################################################
SLL = SinglyLinkedList()

# Insert Nodes
SLL.prepend(23)
SLL.prepend(45)
print(SLL)







