#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def maxSquare2(self, matrix):
        # write your code here
        m = len(matrix) 
        n = len(matrix[0])
        
        if m == 0 or n == 0:
            return 0 
            
        square = [[0] * n for _ in range(m)]
        zero_row = [[0] * n for _ in range(m)]
        zero_col = [[0] * n for _ in range(m)]

        square_edge = 0 
        
        for r in range(m) :
            for c in range(n) :
                if matrix[r][c] == 0:
                    zero_row[r][c] = 1 
                    zero_col[r][c] = 1 
                    # square[r][c] = 0 
                    if r > 0:
                        zero_row[r][c] += zero_row[r-1][c] 
                    if c > 0:
                        zero_col[r][c] += zero_col[r][c-1] 
                        
                else:
                    
                    # zero_col = zero_row = 0 
                    if r > 0 and c > 0:
                        square[r][c] = min(square[r-1][c-1], zero_row[r-1][c], zero_col[r][c-1]) + 1 
                        
                    else:
                        square[r][c] = 1 
            
            square_edge = max(square_edge, max(square[r]))
            
        return square_edge * square_edge
                        
                