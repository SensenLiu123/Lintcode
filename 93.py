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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        if root is None:
            return True 
            
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False 
            
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right) 
        
        return abs(left_height - right_height ) <= 1 
        
    def get_height (self, node) :
        if node is None:
            return 0 
            
        left_h = self.get_height(node.left) 
        right_h = self.get_height(node.right) 
        
        return max(left_h, right_h ) + 1 