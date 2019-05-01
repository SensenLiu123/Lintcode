#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []
        # self.global_min = 2**31 - 1
        

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack1.append(number)
        
        if not self.stack2 or number < self.stack2[-1]:
            self.stack2.append(number)
        else: # repeat last min value
            self.stack2.append(self.stack2[-1])
        

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack1 or not self.stack2:
            return None 
            
        # pop two stacks 
        top = self.stack1.pop()
        
        self.stack2.pop()
        
        return top
        

    """
    @return: An integer
    """
    def min(self):
        return self.stack2[-1] if self.stack2 else None 
