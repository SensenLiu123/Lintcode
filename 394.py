#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:17:00 2019

@author: sensenliu
"""

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        coins = [False, True, True]
        
        
        for i in range(3, n  + 1 ) :
            coins.append(not coins[i-1] or not coins[i - 2]) 
            
        return coins[n]
