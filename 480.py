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
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        ans = []
        path = ''
        
        self.dfs(root, path, ans) 
        
        return ans  
        
    def dfs(self, node, path, ans) :
        if node is None:
            return 
        
        if not node.left and not node.right:
            ans.append(path + str(node.val))
            return 

        self.dfs(node.left, path + str(node.val) + '->' , ans )
        self.dfs(node.right, path + str(node.val) + '->', ans)
        
