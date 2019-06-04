#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0 
            
            
        m, n = len(matrix), len(matrix[0])    
        dp = [[0] * n  for _ in range (m)]
        
        long_edge = max(matrix[0])
        
        for col in range(n):
            dp[0][col] = matrix[0][col]
            
        for row in range(m):
            dp[row][0] = matrix[row][0]
            
        
        for row in range(1,m) :
            for col in range(1,n) :
                
                if matrix[row][col] > 0:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row -1][col - 1]) + 1 
                else:
                    dp[row][col] =  0 
            
            long_edge = max(long_edge, max(dp[row]) )
            
        return long_edge * long_edge
                    
                    
