#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:40:41 2019

@author: sensenliu
"""

import heapq 
class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        new_arrays = []
        for array in arrays:
            if not array:
                continue
            
            new_arrays.append(sorted(array))
            
        heap = []
        
        for index, array in enumerate(new_arrays):
            heapq.heappush(heap, (-array[-1], index, len(array) - 1))
           
        ans = None  
        for _ in range(k):
            num, array_index, index_in_array = heapq.heappop(heap)
            ans = -num
            #print(ans)
            if index_in_array -1 >= 0:
                heapq.heappush(heap, (-new_arrays[array_index] [index_in_array - 1], array_index, index_in_array - 1 ))
        return ans
    
    
    
    
arr = [[1],[1,2,3,4],[11,10,9,8,7]]

# solution is object
# Solution is class 
solution = Solution()

print(solution.KthInArrays(arr, 5))

