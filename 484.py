#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""
class Solution:
    """
    @param A: An integer array
    @param index1: the first index
    @param index2: the second index
    @return: nothing
    """
    def swapIntegers(self, A, index1, index2):
        
        if index2 > len(A) or index1 > len(A):
            return 
        
        A[index1], A[index2] = A[index2], A[index1]

