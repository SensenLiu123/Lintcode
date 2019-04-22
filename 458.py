#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1 
        if target > nums[-1] or target < nums[0]:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1 
            
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            mid = (start + end ) //2 
            # we wanna return the LAST position 
            # so we move start pointer more frequently 
            
            if target >= nums[mid]:
                start  = mid
            else:
                end = mid 
                
        if nums[end] == target:
            return end 
        if nums[start] == target:
            return start 
        return -1 
    
    

