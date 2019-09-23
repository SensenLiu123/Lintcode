#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:32:34 2019

@author: sensenliu
"""

class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, s):
        # write your code here
        if len(s) == 0 or len(s) == 1:
            return 1 
            
        n = len(s)    
        dp = [[0] * n  for i in range(n)] 
        
        ans = 0 
        
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right -1] == 1):
                    dp[left][right] = 1 
                    
                ans += dp[left][right]
                    
                    
        return ans 
