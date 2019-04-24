#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def connectedSet2(self, nodes):
        self.root_kids = {node.label: [node.label] for node in nodes}
        self.root_hash = {node.label: node.label for node in nodes}
        
        for node in nodes:
            for neighbor in node.neighbors:
                self.union(node.label, neighbor.label)
                
        ans = []
        
        for root in self.root_kids:
            ans.append( sorted (self.root_kids[root]) ) 
            
        return ans
                
                
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return
        
        self.root_hash[root_a] = root_b 
        self.root_kids[root_b] = self.root_kids[root_a] + self.root_kids[root_b]
        del self.root_kids[root_a]

    def find(self, node):
        path = []
        
        while node != self.root_hash[node]:
            path.append(node)
            node = self.root_hash[node]
            
        root = node
        for node in path:
            self.root_hash[node] = root 
            
        return root 
