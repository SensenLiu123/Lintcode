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
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        if root is None:
            return 0 
            
        return self.dfs(root)
        
    def dfs(self, root):
        if root is None:
            return 0 
            
        max_from_left = self.dfs(root.left)
        max_from_right = self.dfs(root.right)
            
        return max(0, max_from_right, max_from_left) + root.val 
        
                
