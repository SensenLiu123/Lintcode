#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0 
            
        m = len(A) 
        n = len(B) 
        
        if m == 0 or n == 0:
            return 0
            
        dp = [[0] * (n + 1)  for _ in range(m + 1 )] 
        
        for r in range(m + 1) :
            for c in range(n + 1) :
                if r == 0 or c == 0:
                    continue  
                
                dp[r][c] = max(dp[r-1][c], dp[r][c-1])
                if A[r-1] == B[c-1]:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c - 1] + 1) 
                    
        return dp[m] [n]
        
        
