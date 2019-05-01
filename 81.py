#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

import heapq 
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        ans = []

        max_heap = []
        min_heap = []
        
        for i in range(len(nums)):
            if not max_heap or nums[i] < -max_heap[0]:
                heapq.heappush(max_heap, -nums[i])
            else:
                heapq.heappush(min_heap, nums[i])

            self.balance(max_heap, min_heap)
            ans.append(max_heap[0] * -1)
            
            
        return ans 
        
    def balance(self, max_heap, min_heap):
        # size of max heap == min heap or min_heap + 1 
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
            
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
                
                
        
        
        