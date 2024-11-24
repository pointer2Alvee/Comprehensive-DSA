"""
© alvee 2024
email : pointer2alvee@gmail.com 

Comprehensive Tree Operations/Algorithms :
-------------------------------------------
    
All three have the following operations : 
(1) Creating Tree Node
(2) Traversal
    (2.1) preorder_traversal()
    (2.2) inorder_traversal()
    (2.3) postorder_traversal()
    (2.4) levelorder_traversal()
(3) search()
(4) insert() 
(5) delete()

"""

import Queue as queue
############### Binary Search Tree ###############
class BSTNode:
    
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = self.right_child = None

# (2.1), (2.2), (2.3) Exactly same as Binary Tree

# (2.4) levelorder_traversal()
def levelorder_traversal(root_node):
    if not root_node:
        return
    else:
        levels = queue.QueueThree()
        levels.enqueue(root_node)
        
        while not levels.is_empty():
            
            node = levels.dequeue()
            print(node.data.data) 
            
            if node.data.left_child is not None:
                levels.enqueue(node.data.left_child)
            
            if node.data.right_child is not None:
                levels.enqueue(node.data.right_child) 
        
     
        
# (3.0) search()
def search(root_node, target) -> bool:
    if not root_node:
        return False
    else:
        if target == root_node.data :
            return True
        elif target < root_node.data :
            return search(root_node.left_child, target)
        elif target > root_node.data :
            return search(root_node.right_child, target)
        else:
            return False

        
# (4.0) insert()
def insert(root_node, value):
    if not root_node:
       root_node.data = value
       
    elif value <= root_node.data :
       if (root_node.left_child is None):
           root_node.left_child = BSTNode(value)
       else:
           insert(root_node.left_child,value)
    elif value > root_node.data:
        if (root_node.right_child is None):
             root_node.right_child = BSTNode(value)
        else:
            insert(root_node.right_child, value)
   
    return True
   
   
   
                
# (5.0) delete()

# helper_func : find min
def _get_min_node(bst_node):
    if not bst_node:
        return False
    else:
        curr_node = bst_node
        while curr_node.left_child is not None:
            curr_node = curr_node.left_child
    return curr_node


# delete_node
def delete(root_node, target):
    
    if not root_node:
        return None
    
    # Case - 01: if target is a leaf Node
    if target < root_node.data:
        root_node.left_child = delete(root_node.left_child, target)
    elif target > root_node.data:
        root_node.right_child = delete(root_node.right_child, target)

    # Case - 02 : if target has one child
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        elif root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp
        
        # Case - 03 : Target has both children
        else:
            min_node = _get_min_node(root_node.right_child)
            root_node.data = min_node.data
            root_node.right_child = delete(root_node.right_child, min_node.data)
    return root_node


# delete bst
def delete_bst(root_node):
    if not root_node:
        return False
    else:
        root_node.left_child = root_node.right_child = root_node.data = None
################## Binary Search Tree implementations ##############
####################################################################
# Creating Tree
bst = BSTNode(50)
nd1 = BSTNode(40)
nd2 = BSTNode(60)

nd3 = BSTNode(30)
nd4 = BSTNode(55)

nd5 = BSTNode(45)
nd6 = BSTNode(65)

nd7 = BSTNode(25)

bst.left_child = nd1
bst.right_child = nd2

nd1.left_child = nd3
nd1.right_child = nd4

nd2.left_child = nd5
nd2.right_child = nd6

nd3.left_child = nd7

print("Search() : ")
print(f"node present ? : {search(bst, 30)}")

levelorder_traversal(bst)

print(f"\n_get_min_node() : {_get_min_node(bst).data}")
print(f"\ndelete() : {delete(bst, 60)}")
levelorder_traversal(bst)

print(f"\ninsert() : {insert(bst, 60)}")
print()
levelorder_traversal(bst)


print(f"\ndelete_bst() : {delete_bst(bst)}")
levelorder_traversal(bst)