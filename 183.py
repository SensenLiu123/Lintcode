#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        
        if k > sum(L) or not L:
            return 0 

        max_leng = max(L)
        
        if k <= 1:
            return max_leng
        
        start, end = 1, max_leng 
        
        while start + 1 < end :
            mid = (start + end ) // 2
            
            count = self.cut(L, mid)
            
            if count >= k:
                start = mid 
            else:
                end = mid 
                
                
        if self.cut(L, end) - k > 0:
            return end 
            
        return start 
        
        
    def cut(self, L, length):
        return sum ( [wood // length for wood in L] )
            
