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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        return self.findnode(root, A, B)
        
        
    def findnode(self, root, A, B):
        if root is None:
            return None 
            
        if root.val == A.val or root.val == B.val:
            return root 
            
        find_left = self.findnode(root.left, A, B)
        
        find_right = self.findnode(root.right, A, B)
        
        # now decide the lca 
        if find_left and find_right:
            return root 
            
        if not find_left:
            return find_right
            
        if not find_right:
            return find_left
            
        return None 
        
