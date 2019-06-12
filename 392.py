#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A or len(A) == 0:
            return 0 
            
        if len(A) == 1:
            return A[0]
         
        n = len(A)    
        dp = [0] * n  
        
        dp[0], dp[1] = A[0], max(A[0], A[1])
            
        for i in range(2, n) :
            dp[i] = max(dp[i-1], dp[i-2]  + A[i])
            
        return dp[n-1]