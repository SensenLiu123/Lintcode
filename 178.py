#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    
    def validTree(self, n, edges):
        if len(edges) != n-1:
            return False
            
        self.count = n 
        self.root_array = [i for i in range(n)]
        
        # tree: no loop and one root node 
        for edge in edges:
            loop = self.union(edge[0], edge[1])
            if loop:
                return False 
            
        return self.count == 1 
        
    def union(self, a, b):
        # return true is there is loop, other wise false 
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return True 
            
        self.root_array[root_b] = root_a
        self.count -= 1 
        return False 
        
        
    def find(self, node):
        path = []
        while node != self.root_array[node]:
            path.append(node)
            node = self.root_array[node]
            
        root = node
        for node in path:
            self.root_array[node] = root 
            
        return root 
            

