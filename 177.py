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
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        if not A:
            return None ; 
            
        return self.convert(A) 
            
    def convert(self, array) :
        if not array:
            return None 
            
        middle = ( len(array )-1 ) // 2 
        
        root = TreeNode(array[middle] )
        root.left = self.convert( array[: middle] )
        root.right = self.convert( array[middle + 1 :] )
        
        return root 
        
