#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""
import heapq 
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        m,n = len(matrix), len(matrix[0])
        
        if k > m*n:
            return 
        
        heap = []
        visited = set()
        
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        visited.add((0,0))
        
        
        for _ in range(k):
            ans, x, y = heapq.heappop(heap)
            
            for dx, dy in [(0,1), (1,0)]:
                xx, yy = x+ dx, y + dy
                
                if xx >=m or yy >= n or (xx, yy) in visited:
                    continue
                
                heapq.heappush(heap, (matrix[xx][yy], xx, yy))
                visited.add((xx,yy))
        return ans 
    
    
