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
class ListNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next 

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head   
            
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        node = head 
        
        while node:
            
            # we reach the tail of the list~~ 
            if node.next is None:
                break
            
            # if node and next are distinct values 
            while node.next and node.next.val != node.val:
                node = node.next
                prev = prev.next
                continue
            
            # we meet duplicates.
            while node.next and node.next.val == node.val:
                node.next = node.next.next
                
            node = node.next 
            
            # then remove the first duplicate 
            prev.next = prev.next.next 
            continue 
            
            
        return dummy.next 
        
test = Solution()
# 0 1 1 2 3 None Linked List
head = ListNode(0)
node = head 
node.next = ListNode(1)
node = node.next 
node.next = ListNode(1)
node = node.next 
node.next = ListNode(2)
node = node.next 
node.next = ListNode(3)
node = node.next 
print(head)
test.deleteDuplicates(head)