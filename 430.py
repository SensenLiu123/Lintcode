#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        if len(s1) != len(s2) :
            return False  
            
        return self.dfs(s1, s2)
        
        
    def dfs(self, s1, s2):
        if len(s1) != len(s2) :
            return False 
            
        if len(s1) == 1:
            return s1 == s2 
            
        # pruning 
        char_array1 = sorted(list(s1)) 
        char_array2 = sorted(list(s2)) 
        for i in range(len(char_array1)):
            if char_array1[i] != char_array2[i]:
                return False 
        
        
        #########
        n = len(s1)    
            
        for i in range(1, len(s1)) :
            case1 = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) 
            
            case2 = self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i])

            if case1 or case2:
                return True 
                
        return False 
        
        
    