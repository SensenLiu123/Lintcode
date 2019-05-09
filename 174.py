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
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if not head:
            return None 
            
        fast, slow = head, head 
        
        for _ in range(n):
            fast = fast.next 
            if fast is None:
                return head.next   
        
        
        # to remove slow node, we stop at slow -1 node
        # so while fast.next, not while fast
        while fast.next:
            slow = slow.next 
            fast = fast.next 
            
        slow.next = slow.next.next 
        return head 
