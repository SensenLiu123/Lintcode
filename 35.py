#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:09:17 2019

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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if head is None:
            return None 
        prev = None 
        
        node = head 
        
        while node:
            future = node.next 
            
            node.next = prev 
            
            prev = node
            node = future 
            
        return prev  
