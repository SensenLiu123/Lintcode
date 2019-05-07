#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack  = []
        n = len(s)
        
        if n <= 1:
            return s 
          
        i = 0    
        while i < n:
            # find a digit 
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1 
                stack.append(str(num))
                continue 

            # i should be a [   
            if s[i] == '[':
                i += 1 
                continue
            
            # find chars     
            if s[i].isalpha():
                string = ''
                while i < n and s[i].isalpha():
                    string += s[i]
                    i += 1 
                stack.append(string)
                continue
            
            # meet a ]    
            if s[i] == ']':
                pattern = ''
                
                # pop stack until we meet a digit string 
                while stack and not stack[-1].isdigit():
                    pattern = stack.pop() + pattern
                    
                count = stack.pop()    
                repeat = pattern * int(count)
                stack.append(repeat)
                i += 1 
                continue 
                
        ans = ''
        while stack:
            ans = stack.pop() + ans 
            
        return ans 
        
        
                
            
            
            
            
                
