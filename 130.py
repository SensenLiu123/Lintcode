#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        #for i in range(len(A)):
        #    self.siftup(A,i)
        n = len(A)
        for i in range((len(A)-1) // 2, -1, -1):
            self.siftdown(A,i, n)
    
    # sift up: 从son 求father 比大小        
    def siftup(self,A,son):
        while son > 0:
            father = (son-1)//2
            if A[father] < A[son]:
                break 
            A[father] , A[son] =  A[son], A[father] 
            son = father
            
    # sift down 从father 求小一点的son 比大小        
    def siftdown(self, A, dad, n):
        while dad * 2 + 1 < n:
            son = dad * 2 + 1 
            
            if 2 * dad + 2 < n and A[2 * dad + 2] < A[son]:
                son = 2 * dad + 2 
            
            if A[dad] < A[son]:
                break 
            
            A[son], A[dad] = A[dad], A[son]
            dad = son 