#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid:
            return 0 
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0:
                    dp[i][j] = grid[i][j]  
                    continue
                
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    continue 
                if j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    continue 
                
                dp[i][j] = min(dp[i-1][j] , dp[i] [j-1] ) + grid[i][j] 
        
        return dp[m-1][n-1]
                    
                    
                
        
