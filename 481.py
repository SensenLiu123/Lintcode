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
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        self.ans = 0 
        self.dfs(root) 
        return self.ans 
        
    def dfs(self, node) :
        if node is None:
            return 
        
        # if its a leave node 
        if not node.left and not node.right:
            self.ans += node.val 
            
        self.dfs(node.left )
        self.dfs(node.right) 
        
        
