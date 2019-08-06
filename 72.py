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
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None 
            
        if len(inorder) != len(postorder):
            return None 
            
            
        return self.buildBiTree(inorder, postorder) ;
        
        
        
    def buildBiTree(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None 
            
        rootValue = postorder[-1] 
        
        root = TreeNode(rootValue)
        
        rootIdx = inorder.index(rootValue)
        
        root.left = self.buildBiTree(inorder[:rootIdx], postorder[:rootIdx])
        
        root.right = self.buildBiTree(inorder[rootIdx + 1 :], postorder[rootIdx : -1])
        
        
        return root 
