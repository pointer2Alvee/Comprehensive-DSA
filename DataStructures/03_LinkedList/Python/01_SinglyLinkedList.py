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
        self.head = self.tail =  None
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
        
        if self.head is None:
            self.head = self.tail = new_node  
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    
    # (2.2) insert() method
    def insert(self, data, index) -> bool:
        """
        Inserts node at any given index in the SLL. Edge cases handled
        """
        new_node = Node(data)
        
        
        if index < 0 or index > self.length:
            return False
        
        if self.head is None:
            self.head = self.tail = new_node
            return
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                
            elif index == self.length:
                self.tail.next = new_node
                new_node.next = None
                self.tail = new_node
            
            else:
                curr_node = self.head
                for _ in range(index-1):
                    curr_node = curr_node.next
                
                new_node.next = curr_node.next
                curr_node.next = new_node
            
        self.length += 1
        return True
        
    
    # (2.3) append() method
    def append(self, data)-> bool:
        """
        Adds a new Node in the end of the SLL. Edge cases handled
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
            return
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node
        
        self.length += 1  
        return True  

    
    # (3.0) traverse() method
    def traverse(self):
        """
        Traverses all the nodes of the SLL
        """
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
            
            
    # (4.0) search() method
    def search(self, target)->int:
        """
        Searches for a particular node in the SLL. If found Return TRUE or Index of the Node
        """
        idx = 0
        curr_node = self.head
        while curr_node:
            if(curr_node.data == target):
                return idx
            curr_node = curr_node.next
            idx += 1
        return False


    # (5.0) get() method
    def get(self, index) -> Node:
        """
        Get the node for the given index
        """
        
        if index < 0 or index >= self.length:
            return None
        
        else:
            curr_node = self.head
            for _ in range(index):
                curr_node = curr_node.next
            return curr_node
            
    
    # (6.0) set() method
    def set(self, data, index) -> bool:
        """
        Sets Data on the given index by calling get() method, 
        boundary egde case handled inside get()
        """
        curr_node = self.get(index) 
        if curr_node:
            curr_node.data = data
            return True
        return False
    
    
    # (7.1) pop_first() method
    def pop_first(self) -> Node:
        """
        Pops the first node from the SLL
        """
        
        if self.length == 0:
            return None
        
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = popped_node.next
            popped_node.next = None
            
        self.length -=1 
        return popped_node
    
    
    # (7.2) pop() method
    def pop(self) -> Node:
        """
        Pops the last node from the SLL
        """    
        
        if self.length == 0:
            return None
        
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            curr_node = self.head
            while curr_node.next is not self.tail:
                curr_node = curr_node.next
            
            curr_node.next = None
            self.tail = curr_node
        
        self.length -= 1
        return popped_node 
        
        
    # (7.3) remove() methodd
    def remove(self, index) -> Node:
        """
        To remove any particualt Node in the SLLL
        """
        
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            curr_node = self.get(index-1) # get prev_node of the to be popped_node
            popped_node = curr_node.next
            curr_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node 
        
    # (7.4) delete() method
    def delete(self) -> bool:
        """
        Deletes the entire SLL
        """
        self.head = self.tail = None
        self.length = 0
        return True

################## SLL implementations #################
########################################################
SLL = SinglyLinkedList()
print("starts here:")
# Insert Nodes
print(f"len: {SLL.length}, SLL : {SLL}")

SLL.prepend(23)
print(f"len: {SLL.length}, SLL : {SLL}")

SLL.prepend(45)
print(f"len: {SLL.length}, SLL : {SLL}")

SLL.append(34)
print(f"len: {SLL.length}, SLL : {SLL}")

#print("debug:")
SLL.insert(81,1)
print(f"len: {SLL.length}, SLL : {SLL}")
SLL.insert(66,0)
SLL.insert(9,5)
print(f"len: {SLL.length}, SLL : {SLL}")

SLL.append(42)
print(f"len: {SLL.length}, SLL : {SLL}")

SLL.insert(19,5)
SLL.append(41)
SLL.prepend(322)
print(f"len: {SLL.length}, SLL : {SLL}")

SLL.insert(66,9)

print(f"len: {SLL.length}, SLL : {SLL}")

print(f"(3.0) Traversing :")
#SLL.traverse()


print(f"(4.0) Searching :")
print(f"item at idx : {SLL.search(9)}")

print(f"(5.0) get :")
print(f"item is : {SLL.get(4).data}")

print(f"(6.0) set :")
print(f"item set : {SLL.set(555,5)}")
print(f"len: {SLL.length}, SLL : {SLL}")

print(f"(7.1) pop_first() :")
print(f"item popped : {SLL.pop_first().data}")
print(f"len: {SLL.length}, SLL : {SLL}")

print(f"(7.2) pop() :")
print(f"item popped : {SLL.pop().data}")
print(f"len: {SLL.length}, SLL : {SLL}")

print(f"(7.3) remove() :")
print(f"item popped : {SLL.remove(3).data}")
print(f"len: {SLL.length}, SLL : {SLL}")


print(f"(7.4) delete() :")
print(f"SLL deleted? : {SLL.delete()}")
print(f"len: {SLL.length}, SLL : {SLL}")

