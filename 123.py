#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

DIR = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        if not word:
            return True 
            
        m,n = len(board), len(board[0])   
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, word, 0, m, n, visited, board):
                    return True 
                        
        return False 
        
    def dfs(self, x, y, word, index, m, n, visited,board):
        if index >= len(word):
            return True 
            
        if x >= m or x < 0 or y >= n or y < 0:
            return False 
            
        if (x,y) in visited:
            return False 
        
        if board[x][y] != word[index]:    
            return False 
            
        visited.add( (x,y) )  
        
        for dx, dy in DIR:
            xx, yy = x + dx, y + dy
            
            if self.dfs(xx, yy, word, index + 1 ,m, n, visited,board):
                return True 
                
        visited.remove( (x,y) )     
        return False 
