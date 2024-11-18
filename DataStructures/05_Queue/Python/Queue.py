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


################## Queue implementations #################
##########################################################






############### (C) Queue Linked List ###############################
#####################################################################


################## Queue implementations #################
##########################################################