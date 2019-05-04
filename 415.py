#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        if len(s)<=1:
            return True 
            
        s = s.lower()
        
        left, right = 0, len(s) - 1    
        while left < right:
            while left < right and  not s[left].isalpha() and not s[left].isdigit():
                left += 1 
            while left < right and not s[right].isalpha() and not s[right].isdigit():
                right -= 1 
                
            if s[left] != s[right]:
                return False 
            else:
                left += 1 
                right -= 1 
                
        return True 
