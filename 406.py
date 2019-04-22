#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if not nums:
            return -1 
            
        leng = sys.maxsize 
        running_sum = 0
        left = 0
        
        for right in range(len(nums)):
            running_sum += nums[right]
            
            while running_sum >=s:
                leng = min(leng, right - left + 1)
                running_sum -= nums[left]
                left += 1
                
        return leng if leng < sys.maxsize else -1 
                
            

