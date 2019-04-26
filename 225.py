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
    @param: head: the head of linked list.
    @param: val: An integer.
    @return: a linked node or null.
    """
    def findNode(self, head, val):
        if head is None:
            return None 
            
        node = head
        while node:
            if node.val == val:
                return node 
            node = node.next 
            
        return None 