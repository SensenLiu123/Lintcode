#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        
        return self.dfs(a, b) 
        
    def dfs(self, node_a , node_b) :
        if not node_a:
            return not node_b 
            
        if not node_b: 
            return not node_a 
        
        if node_a.val != node_b.val :
            return False 
            
        subtree_left = self.dfs(node_a.left, node_b.left) 
        if not subtree_left:
            return False 
            
        return self.dfs(node_a.right, node_b.right)
        
