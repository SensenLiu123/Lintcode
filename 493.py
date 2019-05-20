#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:32:56 2019

@author: sensenliu
"""

# class ListNode():
#     def __init__(self,  val) :
#         self.val = val ;
#         self.next = None 
#         self.prev = None 

class Dequeue:
    
    def __init__(self):
        # do intialization if necessary
        self.dummy = ListNode(-1) 
        self.tail = self.dummy 
        

    """
    @param: item: An integer
    @return: nothing
    """
    def push_front(self, item):
        if not self.dummy.next:
            self.push_back(item)
            return 
        
        new_node = ListNode(item)
        head = self.dummy.next 
        
        self.dummy.next = new_node
        new_node.next = head 
        head.prev = new_node
        new_node.prev = self.dummy 

    """
    @param: item: An integer
    @return: nothing
    """
    def push_back(self, item):
        new_node = ListNode(item) 
        
        self.tail.next = new_node
        
        new_node.prev = self.tail 
        
        self.tail = self.tail.next 
        

    """
    @return: An integer
    """
    def pop_front(self):
        if not self.dummy.next:
            return -1 
            
        ans = self.dummy.next.val 
        
        if self.dummy.next == self.tail:
            self.tail = self.dummy 
            self.dummy.next = None 
            #return ans 
            
        else :
            self.dummy.next = self.dummy.next.next 
            self.dummy.next.prev = self.dummy 
        
        return ans 
        
        

    """
    @return: An integer
    """
    def pop_back(self):
        if self.tail == self.dummy:
            return -1 
        
        ans = self.tail.val ;
        
         
        self.tail = self.tail.prev
        self.tail.next = None
        
        return ans 
        
        
