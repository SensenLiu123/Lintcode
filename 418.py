#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:55:07 2019

@author: sensenliu
"""

class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        
        One = ['', 'I', "II", 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        Ten = ['', 'X','XX', 'XXX', 'XL', 'L', "LX", 'LXX', 'LXXX', 'XC']
        Hundred = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC','DCCC', 'CM']
        Thousand = ['', 'M', 'MM', 'MMM','MMMM']
        
        Table = [One, Ten, Hundred, Thousand]
        

        if n == 0:
            return ""
            
        ans = ""
        
        power = 0 ;
        
        while n > 0 :
            digit = n % 10
            
            ans = Table[power] [digit] + ans 
            
            n //=10 
            power += 1 ; 
            
        return ans 
            
            
            
