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
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        dummy = ListNode (-1) 
        
        
        node = head 
        while node:
            cur = dummy 
            
            while cur.next and cur.next.val < node.val:
                cur = cur.next 
                
            tmp = cur.next 
            cur.next = ListNode(node.val)
            cur.next.next = tmp 
            
            node = node.next 
            
        return dummy.next 
                
            
            
            
        
    #     dummy.next  = head 
        
    #     node = head 
        
    #     while node:
    #         self.insertion_sort(dummy, node)
    #         node = node.next 
            
    #     return head  
        
    # def insertion_sort(self, dummy, node) :
    #     if node == dummy.next:
    #         return  
    
            
    #     cur = dummy
    #     while cur.next != node:
    #         if cur.next.val < node.val:
    #             cur = cur.next 
            
    #     tmp = cur.next
    #     cur.next = node 
    #     node.next = tmp 
        
    #     return
    
