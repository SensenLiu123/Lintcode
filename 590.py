#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.root_array = [i for i in range(n + 1)]
        self.root_kid = {i: 1 for i in range(n + 1)}

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return 
        
        self.root_array[root_a] = root_b
        self.root_kid[root_b] += self.root_kid[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        root = self.find(a)
        
        return self.root_kid[root]

    def find(self, node):
        path = []
        
        while node != self.root_array[node]:
            path.append(node)
            node = self.root_array[node]
            
        root = node
        for node in path:
            self.root_array[node] = root 
            
        return root 