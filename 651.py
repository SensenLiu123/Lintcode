#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:02:31 2019

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
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        if root is None:
            return []
        nodePos = []
        
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, pos = queue.popleft()
            
            nodePos.append((node.val, pos))
            
            if node.left:
                queue.append((node.left, pos - 1 ))
                
            if node.right:
                queue.append((node.right, pos + 1 ))
                
                
        nodePos = sorted(nodePos , key = lambda x:x[1])
        ans = []
        for i in range(len(nodePos)):
            
            if i == 0 or nodePos[i][1] > nodePos[i-1][1]:
                ans.append([nodePos[i][0]])
                
            else:
                ans[-1].append(nodePos[i][0])
                
        return ans 
                
                
                
            
        
        
        
    #     self.dfs(root, nodePos, 0)
        
    #     nodePos = sorted(nodePos , key = lambda x:x[1])
        
    #     ans = []
        
    #     for i in range(len(nodePos)):
            
    #         if i == 0 or nodePos[i][1] > nodePos[i-1][1]:
    #             ans.append([nodePos[i][0]])
                
    #         else:
    #             ans[-1].append(nodePos[i][0])
                
    #     return ans 
        
        
        
        
    # def dfs(self, node, nodePos , position):
    #     if node is None:
    #         return 
        
    #     nodePos.append((node.val, position))
        
    #     self.dfs(node.left, nodePos, position - 1)
    #     self.dfs(node.right, nodePos, position + 1)
        
        
        
        
