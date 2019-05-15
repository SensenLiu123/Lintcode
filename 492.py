#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:05:45 2019

@author: sensenliu
"""

class ListNode:
    def __init__(self, val):
        self.val = val ;
        self.next = None 

class MyQueue:
    
    def __init__(self):
        self.dummy = ListNode(-1)
        self.tail = self.dummy 
    
    """
    @param: item: An integer
    @return: nothing
    """
    
    
    def enqueue(self, item):
        
        self.tail.next = ListNode(item) 
        self.tail = self.tail.next 
        
        return 

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.dummy.next is None:
            return -1 
        
        if self.dummy.next == self.tail:
            self.tail = self.dummy 
            
        ans = self.dummy.next.val 
        
        self.dummy.next = self.dummy.next.next 
        
        return ans 
        
