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
    @return: true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        return self.dfs(a, b) 
        
        
    def dfs(self, a, b) :
        if a is None:
            return b is None 
            
        if b is None:
            return False 
        
        if a.val != b.val:
            return False 
        
        # if no tweak , then left == left , right == right 
        if self.dfs(a.left, b.left):
            return self.dfs(a.right, b.right)

        # tweaked, left == right, right == left 
        elif self.dfs(a.left, b.right):
            return self.dfs(a.right, b.left)
           
        # false     
        else:
            return False 
        
        
        
        
