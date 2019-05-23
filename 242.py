#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if root is None:
            return [] 
            
        queue = collections.deque([root])
        
        ans = []
        while queue:
            dummy = ListNode(-1)
            tail = dummy 
            for _ in range(len(queue)):
                tree_node = queue.popleft() ;
                
                new_node = ListNode(tree_node.val)
                tail.next = new_node 
                tail = tail.next 
                
                if tree_node.left:
                    queue.append(tree_node.left) 
                if tree_node.right:
                    queue.append(tree_node.right)
                    
                    
            ans.append(dummy.next )
            
            
        return ans 