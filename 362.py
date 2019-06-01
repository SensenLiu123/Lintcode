#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:41:04 2019

@author: sensenliu
"""

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
            
        if k ==  1:
            return nums 
        if k >= len(nums) :
            return [max(nums)]
        
        dequeue = collections.deque()
        
        # k - 1 以后就要开始pop 最大值了 所以不能到 k！
        # 从k -1 开始就放max 进ans 中
        for i in range(k - 1) :
            self.push(dequeue, nums, i) 
            
          
        ans = []    
        for i in range(k - 1 , len(nums)):
            self.push(dequeue, nums, i) 
            
            max_value = nums[dequeue[0]]
            ans.append(max_value)
            
            if dequeue[0] == i - k + 1:
                dequeue.popleft()
                
        return ans 
            
            
            
    def push(self, dequeue, nums, i) :
        while dequeue and nums[ dequeue[-1] ] < nums[i]:
            dequeue.pop() 
            
        dequeue.append(i)
            
