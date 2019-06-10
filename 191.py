#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        if not nums:
             return None 
          
        n = len(nums) 

        dp_max = [0] * n 
        dp_min = [0] * n 
        
        ans = nums[0] 
        
        for i , num in enumerate (nums):
            
            if i == 0:
                dp_max[i] = num 
                dp_min[i] = num
                continue 

            dp_max[i] = max(num, dp_max[i-1] * num, dp_min[i-1] * num) 
            dp_min[i] = min(num, dp_max[i-1] * num, dp_min[i-1] * num)
            
            if dp_max[i]  > ans:
                ans = dp_max [i]
                
                
        return ans 
            
             
        
            
