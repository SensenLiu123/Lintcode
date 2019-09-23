#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:02:47 2019

@author: sensenliu
"""

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        
        m,p,n = len(A), len(A[0]), len(B[0])
        
        nonzeroA = []
        for r in range(m):
            nonzero = set()
            for c in range(p):
                if A[r][c] == 0:
                    continue 
                nonzero.add(c)
                
            nonzeroA.append(nonzero)
        
        
        nonzeroB = []        
        for c in range(n):
            nonzero = set()
            
            for r in range(p):
                if B[r][c] == 0:
                    continue 
                
                nonzero.add(r)
                
            nonzeroB.append(nonzero)
                
        
        
        C = [[0] * n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                for k in nonzeroA[i] & nonzeroB[j]:
                    
                    C[i][j] += A[i][k]* B[k][j]
                    
        return C 
