#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if x <= 0:
            return 0 
        
    
        
        if x >= 1:
            start, end = 0.0, x 
        else:
            start, end = x, 1.0 
        
        
        eps = 1e-10 
        
        while start + eps < end :
            mid = (start + end ) / 2.0 
            
            if abs(mid * mid - x) < eps:
                return mid 
                
            if mid * mid < x :
                start = mid 
            else:
                end = mid 
                
                
        if (end * end - x) > eps:
            return start 
            
        return end 
                