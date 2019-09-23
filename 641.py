#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:08:44 2019

@author: sensenliu
"""

class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # lower >= upper 
        # lower > nums[0]
        # upper < nums[-1]
        
        if len(nums) == 0 or not nums:
            if lower == upper:
                return [str(lower)] ;
            else:
                return [str(lower) + '->' + str(upper)]
            
       
        if lower > upper:
            return []
            
        ans = []
        
        for i in range(len(nums)):
            if i == 0:
                interval = self.getInter(lower - 1, nums[i])
                if interval:
                    ans.append(interval)
                
            if i == len(nums) - 1:
                interval = self.getInter(nums[i], upper + 1)
                
            else:
                interval = self.getInter(nums[i], nums[i+1])
            
            if len(interval) == 0:
                continue ;
                
            ans.append(interval)        
        
        return ans 
        

    def getInter(self, low, high):
        if high - low == 2:
            return str(low + 1)
            
        if high - low < 2:
            return ""

        
        return str(low + 1) + '->' + str(high - 1)
            
            
            
            
