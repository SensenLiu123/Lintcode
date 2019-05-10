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
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return None 
            
        node = head
        
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next 
                
            node = node.next     
            
        return head 
        
