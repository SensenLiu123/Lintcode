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
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        if head is None:
            return True 
            
        mid = self.find_middle(head)
        
        # middle 重新指针到链表尾巴，逆链表！
        mid.next = self.reverse(mid.next)
        
        node1, node2 = head, mid.next 
        while node2:
            if node1.val != node2.val:
                return False 
            node1 = node1.next 
            node2 = node2.next 
            
        return True 
                
                
    def find_middle(self, head):
        slow, fast = head, head.next 
        
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            
        return slow 
        
    def reverse(self, head):
        prev = None 
        node = head 
        
        while node:
            future = node.next 
            
            node.next = prev 
            
            prev = node
            node = future
            
        return prev 
