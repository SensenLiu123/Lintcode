#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:30:04 2019

@author: sensenliu
"""
# selection sort 
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        self.selectionsort(A) 
        
    def selectionsort(self, A):
        for i in range(len(A)):
            min_idx = i 
            
            for j in range(i+1, len(A)):
                if A[j] < A[min_idx] :
                    min_idx = j 
                    
            A[min_idx], A[i] = A[i], A[min_idx] 
            
# bubble sort    
#class Solution:
#    """
#    @param A: an integer array
#    @return: nothing
#    """
#    def sortIntegers(self, A):
#        self.bubblesort(A)
#        
#    def bubblesort(self, A):
#        
#        n = len(A)
#        for i in range(n):
#            for j in range(n - i - 1):
#                if A[j] > A[j+1]:
#                    A[j], A[j+1] = A[j+1], A[j]
#                    
                    
