#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

import heapq 

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        max_heap, min_heap = [],[]
        ans = []
        
        for i in range(len(nums)):
            
            if not max_heap or nums[i] < -max_heap[0]:
                heapq.heappush(max_heap, -nums[i])
            else:
                heapq.heappush(min_heap, nums[i])
                
            self.balance(max_heap, min_heap)    
                
            print(max_heap, min_heap)
            
            if i >= k:
                if nums[i-k] >= min_heap[0]:
                    min_heap.remove(nums[i-k])
                else:
                    max_heap.remove(-nums[i-k])
                                
            
            ans.append(max_heap[0] * -1)
                    
        return ans 
        
        
    def balance(self, max_heap, min_heap):
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, heapq.heappop(min_heap) * -1 ) 
            
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
            
            
solver = Solution()

nums = [1,2,7,7,2];
            
print(solver.medianSlidingWindow(nums, 3))
