#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:41:31 2019

@author: sensenliu
"""

class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        start = 1 
        end = len(nums) - 1  
        
        while start +  1 < end :
            mid = (start + end) // 2 
            
            if self.smaller_equal(nums, mid)  >  mid:
                end = mid 
            else:
                start = mid  
                
        if self.smaller_equal(nums, start) > start:
            return start 
            
        return end  
        
    def smaller_equal(self, nums, guess):
        count = 0 
        for num in nums:
            if num <= guess:
                count += 1  
        return count 