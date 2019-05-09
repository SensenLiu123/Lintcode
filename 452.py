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
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        if head is None:
            return None 
        
        node = head
        
        new_node = dummy = ListNode(-1)
        
        
        while node:
            if node.val != val:
                new_node.next = ListNode(node.val)
                new_node = new_node.next 
                
            node = node.next 
                
        return dummy.next 