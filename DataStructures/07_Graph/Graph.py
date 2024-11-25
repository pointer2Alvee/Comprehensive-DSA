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

# (1) Creating Graph Class
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
            try:
                self.adjacency_list[vertex_one].remove(vertex_two)
                self.adjacency_list[vertex_two].remove(vertex_one)
            except ValueError:
                pass
            return True
        return False
            
            
    # (5) remove_vertex()
    def remove_vertex(self, vertex):
        
        if vertex in self.adjacency_list.keys():
            for edge in self.adjacency_list[vertex]:
                self.adjacency_list[edge].remove(vertex)
            del self.adjacency_list[vertex]
            return True
            
        return False
    
    
    # (6.1) bfs
    def bfs(self,starting_vertex):
        
        visited_vertices = set()
        visited_vertices.add(starting_vertex)
        
        queue = deque([starting_vertex])
        
        while queue:
            curr_vertex = queue.popleft()
            print(f"{curr_vertex} ", sep="-", end="")
            
            for adjacent_vertex in self.adjacency_list[curr_vertex]:
                if adjacent_vertex not in visited_vertices:
                    visited_vertices.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
    
    
    # (6.2) dfs
    def dfs(self, starting_vertex):
        
        visited_vertices = set()
        stack = [starting_vertex]
        
        while stack:
            curr_vertex = stack.pop()
            
            if curr_vertex not in visited_vertices:
                visited_vertices.add(curr_vertex)
                print(f"{curr_vertex} ", sep="", end="")
            
            for adjacent_vertex in self.adjacency_list[curr_vertex]:
                if adjacent_vertex not in visited_vertices:
                    stack.append(adjacent_vertex)        
                    
################# IMPLEMENTING GRAPH ###################

gph = Graph()
gph.add_vertex("A")
gph.add_vertex("B")
gph.add_vertex("C")
gph.add_vertex("D")
gph.add_vertex("E")

gph.add_edge("A", "B")
gph.add_edge("A", "C")

gph.add_edge("C", "D")
gph.add_edge("B", "E")

gph.add_edge("D", "E")

gph.print_graph()
print("\nbfs:")
gph.bfs("A")

print("\ndfs:")
gph.dfs("A")