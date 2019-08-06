#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections 

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        if node is None:
            return None 
            
        if values[node] == target:
            return node 
            
        queue = collections.deque([node])
        visited = set([node])
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                n = queue.popleft()
                if values[n] == target:
                    return n 
                    
                for neighbor in n.neighbors:
                    if neighbor in visited:
                        continue 
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        return None 
                    
                    
