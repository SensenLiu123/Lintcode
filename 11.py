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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        res = []
        
        self.dfs(root, k1, k2, res)
        
        return sorted(res) 
        
        
    def dfs(self, node, a, b, res):
        if node is None:
            return 
        
        if node.val < a:
            self.dfs(node.right, a, b, res)
             
            
        elif node.val > b:
            self.dfs(node.left, a, b, res) 
            
        else:
            res.append(node.val)
            self.dfs(node.left, a, node.val, res)
            self.dfs(node.right, node.val, b, res)
            
        
            
            
