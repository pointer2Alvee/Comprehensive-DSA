"""
© alvee 2024
email : pointer2alvee@gmail.com 

Comprehensive Tree Operations/Algorithms :
-------------------------------------------
** Three Types of Queue Creation 
    (A) Generic Tree
    (B) Binary Tree
    
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


############### (A) Generic Tree ###############

class TreeNode:
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children
       
        
    def __str__(self, level = 0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret         


    def add_child(self, tree_node):
        self.children.append(tree_node)



################## Tree implementations #################
##########################################################
drinks = TreeNode("Drinks", [])
hot = TreeNode("Hot", [])
cold = TreeNode("Cold", [])


alcoholic = TreeNode("Alcoholic", [])
soft_drinks = TreeNode("Soft Drinks", [])


tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])


drinks.add_child(hot)
drinks.add_child(cold)


hot.add_child(tea)
hot.add_child(coffee)

cold.add_child(alcoholic)
cold.add_child(soft_drinks)

print(drinks)



############### (A) Binary Tree ###############
import Queue as queue

class BinaryTree:
    def __init__(self,data) -> None:
        self.data = data
        self.left_child = self.right_child = None
        
    
# (2.1) preorder_traversal()
def preorder_traevrsal(root_node):
    if not root_node:
        return 
    else:
        print(root_node.data)
        preorder_traevrsal(root_node.left_child)
        preorder_traevrsal(root_node.right_child)
    

# (2.2) inorder_traversal()
def inorder_traversal(root_node):
    if not root_node:
        return
    else:
        inorder_traversal(root_node.left_child)
        print(root_node.data)
        inorder_traversal(root_node.right_child)
            
# (2.3) postorder_traversal()
def postorder_traversal(root_node):
    if not root_node:
        return
    else:
        postorder_traversal(root_node.left_child)
        postorder_traversal(root_node.right_child)
        print(root_node.data)
    
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
        

# (3.0) insert()
def insert(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        levels = queue.QueueThree()
        levels.enqueue(root_node)
        
        while not levels.is_empty():
            node = levels.dequeue()
            
            if node.data.left_child is not None:
                levels.enqueue(node.data.left_child)
            else:
                node.data.left_child = new_node
                return True
                
            if node.data.right_child is not None:
                levels.enqueue(node.data.right_child)
            else:
                node.data.right_child = new_node
                return True
        return False


# (4.0) Search()
def search(root_node, target):
    if not root_node:
        return
    else:
        levels = queue.QueueThree()
        levels.enqueue(root_node)
        
        while not levels.is_empty():
            node = levels.dequeue()
            
            if node.data.data == target:
                return True
            
            if node.data.left_child is not None:
                levels.enqueue(node.data.left_child)
            
            if node.data.right_child is not None:
                levels.enqueue(node.data.right_child)
            
        return False      


# (5.0) delete() 

# helper_func : 
def _get_deepest_node(root_node):
    if not root_node:
        return
    else:
        levels = queue.QueueThree()
        levels.enqueue(root_node)
        
        while not levels.is_empty():
            node = levels.dequeue()
            
            if node.data.left_child is not None:
                levels.enqueue(node.data.left_child)
            
            if node.data.right_child is not None:
                levels.enqueue(node.data.right_child)
            
        return node.data # returns a BT node
    
# helper_func
def _del_deepest_node(root_node, deepest_node):
    if not root_node:
        return
    else:
        levels = queue.QueueThree()
        levels.enqueue(root_node)
        
        while not levels.is_empty():
            node = levels.dequeue()
            
            if(node.data is deepest_node):
                node.data = None
                return True
            
            if node.data.left_child is not None:
                if node.data.left_child is deepest_node:
                    node.data.left_child = None
                    return True
                else:
                    levels.enqueue(node.data.left_child)
            
            if node.data.right_child is not None:
                if node.data.right_child is deepest_node:
                    node.data.right_child = None
                    return True
                else: 
                    levels.enqueue(node.data.right_child)
            
        return node.data
        

# delete any node
def delete(root_node, target):
    if not root_node:
        return
    else:
        levels = queue.QueueThree()
        levels.enqueue(root_node)
        
        while not levels.is_empty():
            
            node = levels.dequeue()
            
            if node.data.data == target:
                
                deepest_node = _get_deepest_node(root_node)
                node.data.data = deepest_node.data
                _del_deepest_node(root_node,deepest_node)

                return True
                
                
            if node.data.left_child is not None:
                levels.enqueue(node.data.left_child)
                    

            if node.data.right_child is not None:
                levels.enqueue(node.data.right_child)
                
        return False
   
# delete full tree 
def delete_tree(root_node):
    root_node.data = root_node.left_child = root_node.right_child = None
    return True
                    
################## Binary Tree implementations ##################
##########################################################

# Dummy Tree : 

bt = BinaryTree(45)
lc = BinaryTree(66)
rc = BinaryTree(22)
lc_lc = BinaryTree(9)
lc_rc = BinaryTree(72)
rc_rc = BinaryTree(8)

bt.left_child = lc
bt.right_child = rc

lc.left_child = lc_lc
lc.right_child = lc_rc

rc.right_child = rc_rc

new_node = BinaryTree(3)

# preroder_traversal()
print("Preorder: ")
preorder_traevrsal(bt)

# inorder_traversal()
print("Inorder: ")
inorder_traversal(bt)

# postorder_traversal()
print("postorder: ")
postorder_traversal(bt)

# levelorder_traversal()
print("levelorder: ")
levelorder_traversal(bt)

# insert()
print("insert: ")
insert(bt,new_node)
print("levelorder: ")
levelorder_traversal(bt)

# search()
print("search: ")
print(f"item found? : {search(bt,22)}")

# _get_deepest_node()
print("_get_deepest_node(): ")
print(f"deepest node? : {_get_deepest_node(bt).data}")


# _del_deepest_node()
print("_del_deepest_node(): ")
print(f"deepest node deleted? : {_del_deepest_node(bt,_get_deepest_node(bt))}")
# levelorder_traversal()
print("levelorder: ")
levelorder_traversal(bt)


# _delete_node()
print("del node(): ")
print(f"node deleted? : {delete(bt,66)}")
# levelorder_traversal()
print("levelorder: ")
levelorder_traversal(bt)



# _delete_Tree()
print("del tree(): ")
print(f"tree deleted? : {delete_tree(bt)}")
# levelorder_traversal()
print("levelorder: ")
levelorder_traversal(bt)
