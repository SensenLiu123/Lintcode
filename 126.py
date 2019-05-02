#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0 
        
        m,n = len(matrix), len(matrix[0])
        
        # the first row is a histogram itself, we start from row 1 in the matrix 
        bars = matrix[0] 
        
        area = 0 
        area = self.max_rec_hist(area, bars)
        
        # from row 1 
        # bar heights only accumulate when marix i j == 1 otherwise its 0 
        for i in range(1,m):
            for j, val in enumerate(matrix[i]):
                if val == 0:
                    bars[j] = 0
                else:
                    bars[j] += 1 

            # finished this row, we find a max area 
            area = self.max_rec_hist(area, bars)
            
        return area 
        
    def max_rec_hist(self, area, bars):
        if not bars:
            return 0 
            
        stack = []    
        for right, current_h in enumerate(bars + [0]):
            
            while stack and bars[stack [-1] ] >= current_h:
                rec_h = bars[stack.pop()]
                
                left = stack[-1] if stack else -1 
                
                area = self.max(area, rec_h * (right - left - 1))
                
            stack.append(right)
            
        return area 
        
    def max(self, a, b):
        return a if a >= b else b 
            
        
