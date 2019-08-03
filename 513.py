#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
s@author: sensenliu
"""

"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        
        distance = 0
        
        # if s == t:
        #     return distance
        
        queue = collections.deque([s])
        
        visited = set([s])
        
        while queue:
            
            node = queue.popleft()
            
            if node == t:
                return distance
            
            for neighbor in node.neighbors:
                
                if neighbor in visited:
                    continue

                queue.append(neighbor)
                visited.add(neighbor)
                
            distance += 1 
                
        return -1 
            

        
