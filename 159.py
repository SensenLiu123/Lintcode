#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums: return -1 
        
        if len(nums) == 1: 
            return nums[0]
        
        start, end = 0, len(nums) -1 
        
        target  = nums[-1]
        while start + 1 < end:
            mid = (start + end) //2
            
            if nums[mid] > target:
                start = mid
            else:
                end = mid 
                
        if nums[start] <=nums[end]:
            return nums[start] 
        else:
            return nums[end] 

