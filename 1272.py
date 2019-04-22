#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

import heapq
class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """
    def kthSmallest(self, matrix, k):
        m,n = len(matrix), len(matrix[0])
        
        if k > m*n:
            return None 
            
        heap = []
        visited = set()
        
        heapq.heappush(heap, (matrix[0][0], 0, 0) )
        visited.add((0, 0))
        
        ans = None 
        for _ in range(k):
            value, x, y = heapq.heappop(heap)
            
            ans = value 
            
            for dx,dy in [(0,1), (1,0)]:
                xx, yy = x + dx, y + dy
                
                if xx >= m or yy >= n:
                    continue 
                if (xx, yy) in visited:
                    continue 
                
                heapq.heappush(heap, (matrix[xx][yy], xx, yy) )
                visited.add((xx,yy))
        return ans 
        
