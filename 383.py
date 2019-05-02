#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        if not heights or len(heights) ==1:
            return 0
            
        if len(heights) ==2:
            return self.min(heights[0], heights[1])
            
            
        left, right = 0, len(heights) -1 
        most_water = 0
        while left < right:
            area = self.min(heights[left], heights[right]) * (right - left)
            if area  > most_water:
                most_water = area
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1 
        return most_water
        
    def min(self, a, b):
        return a if a <= b else b 
        
