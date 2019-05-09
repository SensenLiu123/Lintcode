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
    @return: An integer list
    """
    def toArrayList(self, head):
        ans = []


        node = head        
        while node:
            ans.append(node.val)
            node = node.next 
            
        return ans 