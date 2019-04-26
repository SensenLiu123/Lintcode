#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
#Count the numbers of nodes in a linked list when the node value is non-negative odd
#Input: 1->3->5->null
#Output: 3
#Input: 0->null
#Output: 0

class Solution:
    """
    @param head: 
    @return: nothing
    """
    def countNodesII(self, head):
        if head is None:
            return 0 
        
        node = head   
        count = 0
        while node:
            if node.val > 0 and node.val % 2 ==1:
                count += 1 
            node = node.next 
            
        return count 