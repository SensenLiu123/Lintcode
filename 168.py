#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        if not nums:
            return 0 
            
        balloons = [1] + nums + [1] 
        
        n = len(balloons)
        dp = [[0] * n for _ in range(n)]
        
        # for i in range(n - 1):
        #     dp[i][i + 1] = 0 
            
        for interval in range(3, n + 1) :
            for i in range(n - interval + 1):
                
                j = i + interval - 1 
                
                for k in range(i + 1, j) :
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + balloons[i] * balloons[k] * balloons[j]) 
                    
        return dp[0][n-1]