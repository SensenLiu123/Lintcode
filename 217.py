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

class Solution:
    """
    @param head: The first node of linked list.
    @return: Head node.
    """
    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head
            
        pool = set()
        
        node = head
        
        while node:
            if node.val not in pool:
                pool.add(node.val)
            
            while node.next and node.next.val in pool:
                node.next = node.next.next
                
            node = node.next 
            
        return head 
        
        
