"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of complete binary tree
    @return: the number of nodes
    """
    def countNodes(self, root):
        # write your code here
        if root is None:
            return 0 
            
        height = self.getHeight(root) ; 
        
        leaves = self.countLeaves(root, height) ; 
        
        return 2 ** (height - 1 ) - 1 + leaves  ;
        
        
    def getHeight(self, root):
        h = 0 ;
        node = root 
        while node:
            h += 1 
            node = node.left ;
            
            
        return h 
        
        
    def countLeaves(self, root, height):
        
        start, end = 0 , 2 ** (height - 1) - 1 ;
        
        while start + 1  < end:
            mid = (start + end) // 2 ;
            if self.exist(root, mid, height):
                start = mid 
                
            else:
                end = mid 
                
        return end + 1 if self.exist(root, end, height) else start + 1   
        
    def exist(self, node, guess, height):
        
        left, right = 0 , 2 ** (height - 1) - 1 ;
        
        for _ in range(1, height):
            mid = (left + right) // 2 
            if guess > mid:
                node = node.right 
                left = mid + 1  
                
            else:
                node = node.left 
                right = mid 
                
        return node is not None ;
        
