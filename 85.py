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
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        return self.dfs(root, node)

    def dfs(self, node, new_node):
        if node is None:
            return new_node 
            
        if new_node.val < node.val:
            node.left = self.dfs(node.left, new_node) 
        else:
            node.right = self.dfs(node.right, new_node)
            
        return node 
            
            
