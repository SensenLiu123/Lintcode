#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:22:33 2019

@author: sensenliu
"""

MOVE = [(0, 1 ), (0, -1 ), (1, 0 ), ( -1 , 0 )]
class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0 :
            return 0 
        
        memo = {}
        ans = 1
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                ans = max(ans, self.dfs(matrix, x, y ,memo))
                
               
        return ans 
    
    
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
            
        valid_neighbors = self.find_valid_neighbors(matrix, x, y )
        
        # 递归出口在 if xy 比四周都大，则return 1 
        # 但这个可以和拆解融合 like below 
            
        length = 1     
        for (nx, ny) in valid_neighbors:
            if matrix[x][y] >= matrix[nx][ny]:
                continue 
            
            length = max(self.dfs(matrix, nx, ny, memo) + 1 , length) 
    
        memo[(x, y)] = length  
        return length   
        
        
    def find_valid_neighbors(self, matrix , x, y):
        m , n = len(matrix) , len(matrix[0]) 
        
        neighbors = []
        
        for dx, dy in MOVE:
            nx, ny = x + dx, y + dy 
            
            if 0 <= nx < m and 0 <= ny < n: 
                neighbors.append( (nx, ny) )
                
        return neighbors 
        
                    
                
                
                
                
    