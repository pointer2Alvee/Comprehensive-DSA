"""
© alvee 2024
email : pointer2alvee@gmail.com 

Comprehensive Graph Operations/Algorithms :
-------------------------------------------
    
All three have the following operations : 
(1) Creating Graph Class
(2) add_vertex() 
(3) add_edge()
(4) remove_edge()
(5) remove_vertex()
(6) Traversal
    (6.1) bfs()
    (6.2) dfs()
 
"""

############### Graph ###############
from collections import deque 


class Graph:
    def __init__(self, adjacency_list=None) -> None:
        if not adjacency_list:
            adjacency_list = {}
            
        self.adjacency_list = adjacency_list
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} : {self.adjacency_list[vertex]}")
    
    
    # (2) add_vertex()
    def add_vertex(self, vertex):
        
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    
    # (3) add_edge()
    def add_edge(self, vertex_one, vertex_two):
        
        if vertex_one in self.adjacency_list.keys() and vertex_one in self.adjacency_list.keys():
            self.adjacency_list[vertex_one].append(vertex_two)
            self.adjacency_list[vertex_two].append(vertex_one)
            return True
        return False
    
    
    # (4) remove_edge()
    def remove_edge(self, vertex_one, vertex_two):
        if (vertex_one,vertex_two) in self.adjacency_list.keys():
            self.adjacency_list[vertex_one].remove(vertex_two)
            self.adjacency_list[vertex_two].remove(vertex_one)
            return True
        return False
            
        
            
