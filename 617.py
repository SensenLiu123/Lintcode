#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:59:24 2019

@author: sensenliu
"""

class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        start = min(nums) * 1.0 
        end = max(nums)  * 1.0 
        

        while start + 1e-5 < end :
            
            # guess an average 
            mid = (start + end) / 2.0  
            
            if self.exist_higher(nums, mid , k):
                start = mid  
            else:
                end = mid 
                
        return start 
        
        
    def exist_higher(self, nums, ave, k):
        
        prefix = [0];
        
        min_pref = 2 ** 31 - 1
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + num - ave )
            if i < k - 1 :
                continue 
            
            min_pref = min(min_pref, prefix[i- k + 1])
            
            if prefix[-1] - min_pref >= 0:
                return True 
            
