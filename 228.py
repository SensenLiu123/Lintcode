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
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        if head is None:
            return head
            
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow 