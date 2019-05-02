#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
import heapq
class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        min_heap = []
        
        
        # add borders
        m,n = len(heights), len(heights[0])
        visited = set()
        for j in range(n):
            heapq.heappush(min_heap, (heights[0][j], 0, j))
            visited.add( (0, j) )
            heapq.heappush(min_heap, (heights[m-1][j], m-1, j))
            visited.add( (m-1, j) )
            
        for i in range(1,m-1):
            heapq.heappush(min_heap, (heights[i][0], i, 0))
            visited.add( (i, 0) )
            heapq.heappush(min_heap, (heights[i][n-1], i, n-1))
            visited.add( (i, n-1) )
            
        water = 0 
        
        while min_heap:
            lowest, x, y = heapq.heappop(min_heap)

            for dx,dy in DIR:
                nx, ny = x + dx, y + dy 
                
                if (nx, ny) in visited:
                    continue 
                if not self.within(m,n,nx,ny):
                    continue 

                actual_h = max(lowest, heights[nx][ny])
                water += actual_h - heights[nx][ny]
                
                heapq.heappush(min_heap, (actual_h, nx, ny))
                
                visited.add( (nx, ny ) )
                
        return water 
        
        
    def within(self, m, n, x, y):
        return 0 <= x < m and  0 <= y < n 
                
                
                
        
        
