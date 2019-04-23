#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:22:24 2019

@author: sensenliu
"""

class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.root_array = [i for i in range(n+1)]
        
        
    def find(self, n):
        # node number from 1 to n
        # so node 0 is isolated we use 1 - n 
        path = []
        while n != self.root_array[n]:
            path.append(n)
            n = self.root_array[n]
         
        root = n  
        for node in path:    
            self.root_array[node] = root 
        
        return root 
            
    # def union(self, a, b):
    #     root_a = self.find(a)
    #     root_b = self.find(b)
        
    #     if root_a == root_b:
    #         return 
    #     else:
    #         self.root_array[root_b] = root_a

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
        else:
            self.root_array[root_b] = root_a

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        return root_a == root_b
