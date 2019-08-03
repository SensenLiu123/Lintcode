#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, subs):
        
        if len(subs) == 0 or len(s) == 0:
            return len(s)  
            
        queue = collections.deque([s])
        visited = set([s])
        
        
        minLength = len(s)
        
        
        while queue:
            
            string = queue.popleft()
            
            for reduced in self.getReduced(string, subs):

                if reduced in visited:
                    continue 
                
                minLength = min(minLength, len(reduced))
                
                queue.append(reduced)
                visited.add(reduced)
                
        return minLength 
        
    def getReduced(self, string, subs):
        
        reduced = set()
        
        for substring in subs:
            
            index = string.find(substring)
            
            while index != -1:
                shorter = string[:index] + string[index + len(substring) :]
                
                reduced.add(shorter)
                
                index = string.find(substring, index + 1 )
                
                
        return list(reduced)
                
                
                
                
                    
        
