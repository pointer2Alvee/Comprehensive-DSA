"""
© alvee 2024
email : pointer2alvee@gmail.com 

Comprehensive Stack Operations/Algorithms :
-------------------------------------------
** Three Types of Stack Creation 
    (A) Stack python List - No Size limit
    (B) Stack python List - Size limit
    (C) Stack Linked List 
    
All three have the following operations : 
(1) Stack-Class
(2) is_empty()
(3) is_Full() 
(4) push()
(5) pop() 
(6) peek()
(7) delete() 

"""

############### (A) Stack python List - No Size limit ###############
#####################################################################

# (1.0) Create Stack Class
class StackOne:

    # Init Empty Stack
    def __init__(self) -> None:
        self.stack = []
    
    
    # Modify __str__() method
    def __str__(self) -> str:
        elements = reversed(self.stack)
        elements = [str(elm) for elm in elements]
        return "\n".join(elements)
    
    
    # (2.0) is_empty() method
    def is_empty(self)-> bool:
        if self.stack == []:
            return True
        else:
            return False
    
    # (3.0) is_Full() method Not needed here
    
    
    # (4.0) push() method
    def push(self, value) -> bool:
        self.stack.append(value)
        return True
    
    
    # (5.0) pop() method
    def pop(self) -> bool:
        if self.is_empty():
            return False
        else:
            return self.stack.pop()

    
    
    # (6.0) peek()
    def peek(self) -> bool:
        if self.is_empty():
            return False
        else:
            return self.stack[-1]

    
    # (7.0) delete()
    def delete(self) -> bool:
        if self.is_empty():
            return False
        else:
            self.stack = []
            return True

################## Stack implementations #################
##########################################################
print("\n Stack - python list no size limit")
# create stack instance
my_stk_one = StackOne()

# push()
my_stk_one.push(5)
my_stk_one.push(67)
my_stk_one.push(31)
my_stk_one.push(7)

print(f"\nstack  : \n{my_stk_one}")

# pop()
print(f"\npopped : {my_stk_one.pop()}")
print(f"\nstack  : \n{my_stk_one}")

# peek()
print(f"\npeek : {my_stk_one.peek()}")
print(f"\nstack  : \n{my_stk_one}")

# delete()
print(f"\ndelete : {my_stk_one.delete()}")
print(f"\nstack  : \n{my_stk_one}")





############### (B) Stack python List - Size limit ##################
#####################################################################

# (1.0) Stack Class
class StackTwo:
    
    # Init Empty Stack with max_size
    def __init__(self, max_size) -> None:
        self.stack = []
        self.max_size = max_size
        
    # modify __str__() method
    def __str__(self) -> str:
        elements = reversed(self.stack)
        elements = [str(elm) for elm in elements]
        return "\n".join(elements)
    
    
    # (2.0) is_empty() method
    def is_empty(self) -> bool:
        if self.stack == []:
            return True
        else: 
            return False
        
    
    # (3.0) is_full() method
    def is_full(self) -> bool:
        if len(self.stack) == self.max_size:
            return True
        else: 
            return False
    
    
    # (4.0) push() method
    def push(self, value) -> bool:
        if self.is_full():
            return False
        else:
            self.stack.append(value)
            return True
            
    
    # (5.0) pop() method
    def pop(self) -> bool:
        if self.is_empty():
            return False
        else:
            return self.stack.pop()
    
    # (6.0) peek() method
    def peek(self) -> bool:
        if self.is_empty():
            return False
        else:
            return self.stack[-1]
        
    
    # (7.0) delete() method 
    def delete(self) -> bool:
        self.stack = []
        return True

################## Stack implementations #################
##########################################################

# stack creation
print("\nStack - python list with size limit : ")
my_stk_two = StackTwo(5)

# push()
my_stk_two.push(11)
my_stk_two.push(9)
my_stk_two.push(6)
my_stk_two.push(55)
my_stk_two.push(24)
print(f"\nstack  : \n{my_stk_two}")


# pop()
print(f"\npopped  : {my_stk_two.pop()}")
print(f"\nstack  : \n{my_stk_two}")

# peek()
print(f"\npeeked  : {my_stk_two.peek()}")
print(f"\nstack  : \n{my_stk_two}")

# is_full()
my_stk_two.push(88)
print(f"\nis_full ? : {my_stk_two.is_full()}  & is_empty ? : {my_stk_two.is_empty()}")

# delete()
print(f"\npeeked  : {my_stk_two.delete()}")
print(f"\nstack  : \n{my_stk_two}")


############### (C) Stack Linked List ###############################
#####################################################################

# Create Node
class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Create Linked List (SLL)
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next
            
    

# (1.0) Create Stack Class
class StackThree:
    
    # Create an empty LL, which acts as a stack
    def __init__(self) -> None:
        self.stack = SinglyLinkedList()
        
    
    # modify __str__()
    def __str__(self) -> str:
        elements = [str(elm.data) for elm in self.stack]
        return "\n".join(elements)
    
    
    # (2.0) is_empty() method
    def is_empty(self) -> bool:
        if self.stack.head is None:
            return True
        else:
            return False
    
    
    # (3.0) is_full() method no needed
    
    # (4.0) push() method
    def push(self, value) -> bool:
        new_node = Node(value)
        new_node.next = self.stack.head
        self.stack.head = new_node
        return True
            
            
    # (5.0) pop() method
    def pop(self) -> int:
        if self.is_empty():
            return False
        else:
            popped_item = self.stack.head.data
            self.stack.head = self.stack.head.next
            return popped_item

    # (6.0) peek() method
    def peek(self)->int:
        if self.is_empty():
            return False
        else:
            return self.stack.head.data
    
    
    # (7.0) delete() method
    def delete(self)-> bool:
        if self.is_empty():
            return False
        else:
            self.stack.head = None
            return True

    
################## Stack implementations #################
##########################################################
# stack creation
print("\nStack - Linked List : ")    
my_stk_three = StackThree()

my_stk_three.push(33)
my_stk_three.push(21)
my_stk_three.push(54)
my_stk_three.push(2)
print(f"\nstack  : \n{my_stk_three}")

print(f"\npop()  : \n{my_stk_three.pop()}")
print(f"\nstack  : \n{my_stk_three}")

print(f"\npeek() : \n{my_stk_three.peek()}")
print(f"\nstack  : \n{my_stk_three}")


print(f"\ndelete() : \n{my_stk_three.delete()}")
print(f"\nstack  : \n{my_stk_three}")

    
    