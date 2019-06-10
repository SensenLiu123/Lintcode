#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0 
            
        n = len(A) 
        
        dp_in = [0] * n 
        dp_de = [0] * n 
        
        for i, num in enumerate(A):
            if i == 0:
                dp_in[i] = 1 
                dp_de[i] = 1 
                continue 
            
            if num > A[i-1]:
                dp_in[i] = dp_in[i-1]  + 1 
                dp_de[i] = 1 
                continue  
            
            if num < A[i-1]:
                dp_in[i] = 1 
                dp_de[i] = dp_de[i-1] + 1 
                continue 
            
        return max(max(dp_de), max(dp_in))
