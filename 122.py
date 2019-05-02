#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        
        height.append(0)
        stack = []
        
        area = 0
        
        for right in range(len(height)):
            
            current = height[right]
            
            while stack and height[stack[-1]] >= current:
                popped_bar_index = stack.pop()
                
                # left is on left of the popped 
                left = stack[-1] if stack else -1 
                
                tmp = height[popped_bar_index] * (right - left - 1)
                area = self.max(area, tmp)
            
            stack.append(right)
            
        return area 
        
    def max(self, a, b):
        return a if a >= b else b 
        
        
        