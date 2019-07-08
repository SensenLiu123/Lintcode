#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:33:12 2019

@author: sensenliu
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    
    def findSubtree(self, root):
        # assume: 
        # in: root node of a tree 
        # do we need to define a tree node ?
        # a tree node has two attributes: left and right 
        # also value 
        # ==========================
        # find the max sum of subtree and return the root!
        # then appraoch is we go thru all the nodes, compare the sum and find it
        # This is a dfs search method 
        # And we gonna use recursion to implement 
        
        self.max_sum = - 2 ** 31 
        self.max_node = None 
        
        if root is None:
            return root 
            
        _ = self.find_sum(root) 
        
        return self.max_node
        
        
        
    def find_sum(self, node) :
        # this function returns the sum of each sub tree
        # it does not care about who is max who is not 
        if node is None:
            node_sum =  0 
            
        else:
            left = self.find_sum(node.left)    
            right = self.find_sum(node.right)
            
            node_sum =  node.val + left  + right 
            
        if node_sum > self.max_sum:
            self.max_sum = node_sum
            self.max_node = node 
            
        return node_sum
            
        
            
          
        
        
        
    