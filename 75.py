#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        start , end = 1, len(A) - 2 
        
        while start + 1 < end :
            mid = (start  + end) // 2 
            
            if A[mid] < A[mid + 1]:
                start = mid 
                
            elif A[mid] < A[mid - 1]:
                end = mid 
                
            else:
                end = mid 
                
        if A[start] > A[end]: 
            return start  
        else:
            return end 