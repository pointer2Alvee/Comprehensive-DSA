"""
© alvee 2024
email : pointer2alvee@gmail.com 

Comprehensive Queue Operations/Algorithms :
-------------------------------------------
** Three Types of Queue Creation 
    (A) Queue python List - No Size limit
    (B) Queue python List - Size limit / Circular Queue
    (C) Queue Linked List 
    
All three have the following operations : 
(1) Queue-Class
(2) is_empty()
(3) is_Full() 
(4) enqueue()
(5) dequeue() 
(6) peek()
(7) delete() 

"""



############### (A) Queue Python List - No size limit ###############
#####################################################################

# (1.0) Queue Class
class QueueOne:
    
    def __init__(self) -> None:
        self.queue = []
    
    # modify __str__() method
    def __str__(self) -> str:
        elements = [str(elm) for elm in self.queue]
        return " ".join(elements)
    
    
    # (2.0) is_empty() method
    def is_empty(self) -> bool:
        if self.queue == []:
            return True
        else:
            return False
    
    # (3.0) is_full Not needed
    
    
    # (4.0) enqueue()
    def enqueue(self, value) -> bool:
        self.queue.append(value)
        return True
    
    # (5.0) dequeue()
    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        else:
            dequeued_item = self.queue[0]
            del self.queue[0]
            return dequeued_item
    
    # (6.0) peek() 
    def peek(self) -> int:
        if self.is_empty():
            return False
        else: 
            return self.queue[0]
        
    
    # (7.0) delete()
    def delete(self) -> bool:
        if self.is_empty():
            return False
        else:
            self.queue = []
            return True


################## Queue implementations #################
##########################################################
my_q_1 = QueueOne()

my_q_1.enqueue(5)
my_q_1.enqueue(7)
my_q_1.enqueue(2)
print(f"Queue : {my_q_1}")

my_q_1.dequeue()
print(f"Queue : {my_q_1}")


print(f"peek: {my_q_1.peek()}")
print(f"is_empty?: {my_q_1.is_empty()}")
print(f"deleted?: {my_q_1.delete()}")
print(f"Queue : {my_q_1}")
print(f"is_empty?: {my_q_1.is_empty()}")
print(f"deQueue? : {my_q_1.dequeue()}")






############### (B) Queue Python List - Size Limit ##################
#####################################################################
# Queue Class
class QueueTwo:
    
    # Init empty queue
    def __init__(self, max_size) -> None:
        
        self.queue = max_size * [None]
        self.max_size = max_size
        self.start = self.top = -1
        
        
    
    
    # __str__() method
    def __str__(self) -> str:
        elements = [str(elm) for elm in self.queue]
        return " ".join(elements)
    
    
    # (2.0) is_empty()
    def is_empty(self) -> bool:
        if  self.top == -1: 
            return True
        else: 
            return False
    
    
    # (3.0) is_full()
    def is_full(self) -> bool:
        if (self.top+1 == self.start) or (self.start == 0 and self.top+1 == self.max_size) :
             return True
        else:
            return False
    
    
    # (4.0) enqueue()
    def enqueue(self, value) -> bool:
        
        if self.is_full():
            return False    
        else: 
            if self.top+1 == self.max_size:
                self.top = 0
            else :
                self.top += 1
                if self.start == -1:
                    self.start = 0     
            self.queue[self.top] = value    
            
    
    # (5.0) dequeue()
    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        else:
            dequeued_item = self.queue[self.start]
            self.queue[self.start] = None
            
            if self.start == self.top:
                self.start = self.top = -1
            elif self.start+1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
                
            return dequeued_item
             
         
    # (6.0) peek()
    def peek(self) -> None:
        if self.is_empty():
            return False
        else:
            return self.queue[self.start]
    
    
    # (7.0) delete()
    def delete(self) -> bool:
        if self.is_empty():
            return False
        else:
            self.queue = self.max_size * [None]
            self.start = self.top = -1
            return True
        




################## Queue implementations #################
##########################################################
my_q_2 = QueueTwo(5)
print("\nQueue python list - with size limit: ")
my_q_2.enqueue(9)
my_q_2.enqueue(1)
my_q_2.enqueue(8)
my_q_2.enqueue(5)
my_q_2.enqueue(4)

print(f"Queue : {my_q_2}")
print(f"isFull? : {my_q_2.is_full()}")
print(f"enQueue : {my_q_2.enqueue(2)}")
print(f"Queue : {my_q_2}")

print(f"deQueued : {my_q_2.dequeue()}")
print(f"deQueued : {my_q_2.dequeue()}")
print(f"Queue : {my_q_2}")

print(f"peek : {my_q_2.peek()}")





############### (C) Queue Linked List ###############################
#####################################################################
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
    def __str__(self) -> str:
        return str(self.data)


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None
        
    
    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next
    

class QueueTree:
    def __init__(self) -> None:
        
        self.queue = SinglyLinkedList()
        
        
    def __str__(self) -> str:
        elements = [str(elm) for elm in self.queue]
        return " ".join(elements)
    
    
    def is_empty(self):
        if self.queue.head == None:
            return True
        else:
            return False
    

    def enqueue(self, value):
        
        new_node = Node(value)
        
        if self.is_empty():
            self.queue.head = self.queue.tail = new_node
        else:
            self.queue.tail.next = new_node
            self.queue.tail = new_node
            return True 


    def dequeue(self):
        
        if self.is_empty():
            return False
        else:
            dequeued_item = self.queue.head.data
            if self.queue.head == self.queue.tail:
                self.queue.head = self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next
            return dequeued_item
        
        
    def peek(self):
        
        if self.is_empty():
            return False
        else:
            return self.queue.head.data

    def delete(self):
        
        if self.is_empty():
            return False
        else:
            self.queue.head = self.queue.tail = None
            return True
        
        


################## Queue implementations #################
##########################################################
my_q_3 = QueueTree()
print("\nQueue Linked list : ")
print(f"is_empty? : {my_q_3.is_empty()}")
my_q_3.enqueue(17)
my_q_3.enqueue(26)
my_q_3.enqueue(99)
my_q_3.enqueue(80)
my_q_3.enqueue(59)

print(f"Queue : {my_q_3}")
print(f"is_empty? : {my_q_3.is_empty()}")
print(f"enQueue : {my_q_3.enqueue(2)}")
print(f"Queue : {my_q_3}")

print(f"deQueued : {my_q_3.dequeue()}")
print(f"deQueued : {my_q_3.dequeue()}")
print(f"Queue : {my_q_3}")

print(f"peek : {my_q_3.peek()}")


