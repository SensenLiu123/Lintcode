#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:42:08 2019

@author: sensenliu
"""

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        
        if abs(x) < 0.0000000001:
            return 0 
            
        if n == 0:
            return 1 

        if n == 1:
            return x 
            
        if n < 0:
            return self.myPow(1.0 / x, -n)
           
           
           
        res = 1 
        power = x 
        
        while n > 0:
            if n % 2 == 1:
                res *= power 
                
            power *= power 
            n //=2 
            
            
        return res 