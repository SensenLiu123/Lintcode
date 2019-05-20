#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:25:50 2019

@author: sensenliu
"""

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        stack = []
        
        pair = {']' : '[', ')' : '(' , '}' : '{'} 
        
        for char in s:
            if char not in pair:
                stack.append(char)
                
            else:
                if not stack:
                    return False 
                right = stack.pop()
                if pair[char] != right:
                    return False 
            
        return len (stack ) == 0      
