#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.root_array = [i for i in range(n + 1)]
        self.count = n 
    
    def find(self, node):
        path = []
        
        while node != self.root_array[node]:
            path.append(node)
            node = self.root_array[node]
            
        root = node
        for node in path:
            self.root_array[node] = root
            
        return root 
    
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return 
        
        self.root_array[root_a] = root_b
        self.count -= 1 
        
    """
    @return: An integer
    """
    def query(self):
        return self.count 
    
    