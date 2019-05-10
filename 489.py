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
    @param: nums: an integer array
    @return: the first node of linked list
    """
    def toLinkedList(self, nums):
        # write your code here
        dummy = node = ListNode(-1)
        
        
        for num in nums:
            node.next = ListNode(num)
            node = node.next 
            
        return dummy.next 