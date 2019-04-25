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


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        
        self.root_kid = {node.label:[node.label] for node in nodes}
        self.root = {node.label:node.label for node in nodes}
        
        
        for node in nodes:
            for neighbor in node.neighbors:
                self.union(node.label, neighbor.label)
        
        ans = []        
        for label in self.root_kid:
            ans.append(sorted(self.root_kid[label]) )
            
        return ans 
                
    def union(self, label_a, label_b):
        # everything is label 
        root_a = self.find(label_a)
        root_b = self.find(label_b)
        
        if root_a == root_b:
            return 
        
        self.root[root_b] = root_a
        
        self.root_kid[root_a] = self.root_kid[root_a] + self.root_kid[root_b]
        del self.root_kid[root_b]
        
    def find(self, label):
        path = []
        
        while label != self.root[label]:
            path.append(label)
            label = self.root[label]
            
        rootlabel = label
        
        for label in path:
            self.root[label] = rootlabel
            
        return rootlabel 
    
                
                
        
                