#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0 
            
        n = len(nums)
        
        # dp is the length of longest incresing 
        dp = [1] * n 

        for i in range(n):
            # for each i, check all the prev that is smaller 
            for prev_i in range(i):
                
                if nums[i] > nums[prev_i]:  
                    dp[i] = max(dp[i] , dp[prev_i] + 1 )
                    

        return max(dp)
                    
