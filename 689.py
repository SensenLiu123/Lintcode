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
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        
        if root is None:
            return None 
            
        minNode = self.find_min(root)
        maxNode = self.find_max(root)
        
        left = minNode
        right = maxNode;
        
        
        
        while left.val < right.val:
            
            testSum = left.val  + right.val 
            
            if testSum == n:
                return [left.val, right.val]
                
                
            if testSum < n:
                left = self.getSuccessor(root, left)
                
            else:
                right = self.getPrecursor(root, right)
                
        return None 
        
        
    def find_min(self, root):
        node = root; 
        ans = None 
        
        while node:
            ans = node 
            node = node.left
            
        return ans 
        
    def find_max(self, root):
        node = root
        ans = None 
        
        while node:
            ans = node
            node = node.right 
            
        return ans 
        
        
    def getSuccessor(self, root, p):
        node = root
        ans = None 
        
        while node:
            if p.val >= node.val:
                node = node.right 
                
            else:
                ans = node
                node = node.left 
                
        return ans 
        
    def getPrecursor(self, root, p):
        node = root 
        ans = None 
        
        while node:
            if p.val <= node.val:
                node = node.left 
                
            else:
                ans = node
                node = node.right 
                
        return ans 
            