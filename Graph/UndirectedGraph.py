# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:55:26 2024

@author: Lenovo
"""

import numpy as np

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))
        self._visited = [0]*vertices
    
    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v] = x
        self._adjMat[v][u] = x
    
    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0
        self._adjMat[v][u] = 0
    
    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0
    
    def vertex_count(self):
        return self._vertices
    
    def edge_count(self):
        return np.count_nonzero(self._adjMat) // 2
    
    def printVertices(self):
        for i in range(self._vertices):
            print(i, end=" ")
    
    def printEdges(self):
        for i in range(self._vertices):
            for j in range(i, self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,"--",j)
    
    def degree(self, u):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[u][i] != 0:
                count = count + 1
        return count
    
    def printAdjMat(self):
        print(self._adjMat)
    
    def DFS(self, u):
        self._visited = [0]*self._vertices
        self._DFS_util(u)
        
        for i in range(self._vertices):
            if self._visited[i]== 0:
                self._DFS_util(i)
    
    def _DFS_util(self, u):
        if self._visited[u] == 0:
            print(u, end = " ")
            self._visited[u] = 1
            for i in range(self._vertices):
                if self._adjMat[u][i] != 0 and self._visited[i] == 0:
                    self._DFS_util(i)

'''
Keep x = 1 to make the unweighted graph
'''

G = Graph(4)
print('Graph Adjacency Matrix')
G.printAdjMat()
print('Vertices: ', G.vertex_count())
print('Edges Count:', G.edge_count())
G.insert_edge(0, 1)
G.insert_edge(0, 2)
G.insert_edge(1, 2)
G.insert_edge(2, 3)
print('Graph Adjacency Matrix')
G.printAdjMat()
print('Edges Count:', G.edge_count())
print('Vertices:')
G.printVertices()
print('Edges:')
G.printEdges()
print('Edges between 1--3:', G.exist_edge(1,3))
print('Edges between 1--2:', G.exist_edge(1,2))
print('Degree of vertex 2:',G.degree(2))
print('Graph Adjacency Matrix')
G.printAdjMat()
G.remove_edge(1,2)
print('Graph Adjacency Matrix')
G.printAdjMat()
print('Edges between 1--2:', G.exist_edge(1,2))
G.remove_edge(2, 3)
G.printAdjMat()
G.DFS(0)
'''
Change x to change the weights of graph edges
'''
G = Graph(4)
print('Graph Adjacency Matrix')
G.printAdjMat()
print('Vertices: ', G.vertex_count())
print('Edges Count:', G.edge_count())
G.insert_edge(0, 1, 11)
G.insert_edge(0, 2, 3)
G.insert_edge(1, 2, 7)
G.insert_edge(2, 3, 39)
print('Graph Adjacency Matrix')
G.printAdjMat()
print('Edges Count:', G.edge_count())
print('Vertices:')
G.printVertices()
print('Edges:')
G.printEdges()
print('Edges between 1--3:', G.exist_edge(1,3))
print('Edges between 1--2:', G.exist_edge(1,2))
print('Degree of vertex 2:',G.degree(2))
print('Graph Adjacency Matrix')
G.printAdjMat()
G.remove_edge(1,2)
print('Graph Adjacency Matrix')
G.printAdjMat()
print('Edges between 1--2:', G.exist_edge(1,2))