#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0 
            
        if len(triangle) == 1:
            return triangle[0][0]
            
        totalLayer = len(triangle)
        memo = {}
            
        return self.findMinPath(triangle, 0, 0,totalLayer, memo)
        
        
    def findMinPath(self, triangle, row, numIdx, totalLayer, memo):
        if (row, numIdx) in memo:
            return memo[(row, numIdx)]
            
        if row == totalLayer - 1:
            memo[(row, numIdx)] = triangle[row][numIdx]
            return memo[(row, numIdx)] 
            
            
        subPathLeft = self.findMinPath(triangle, row + 1 , numIdx, totalLayer, memo)
        subPathRight = self.findMinPath(triangle, row + 1 , numIdx + 1, totalLayer, memo)
        
        memo[(row, numIdx)] = min(subPathRight, subPathLeft) + triangle[row][numIdx]
        
        return memo[(row, numIdx)]
            
            
        
