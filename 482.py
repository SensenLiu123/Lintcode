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
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):
        # write your code here
        self.ans = 0 
        self.dfs(root , 1, level)
        
        return self.ans 
        
    def dfs(self, node, cur, level):
        if node is None or cur > level:
            return 
        
        if cur == level:
            self.ans += node.val 
            
        self.dfs(node.left, cur + 1, level) 
        self.dfs(node.right, cur + 1 , level)
        
