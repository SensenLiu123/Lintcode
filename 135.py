#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
           
        # 反正重复取数， 搞短一点    
        nums = sorted(list(set(candidates)))
        path, result = [], []
        self.dfs(nums, 0, target, path, result)
        return result 
        
    def dfs(self, nums, start, target, path, result):
        if target < 0:
            return 
        
        if target == 0:
            result.append(path[:])
            return  
        
        
        for i in range(start, len(nums)):
            if nums[0] >=0 and nums[i] > target:
                continue 
          
            path.append(nums[i])
            self.dfs(nums, i, target - nums[i], path, result)
            path.pop()