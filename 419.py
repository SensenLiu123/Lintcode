#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:53:58 2018

@author: Sensen
"""

class Solution:
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_d = {}
        roman_d['I'] = 1
        roman_d['V'] = 5
        roman_d['X'] = 10
        roman_d['L'] = 50 
        roman_d['C'] = 100
        roman_d['D'] = 500
        roman_d['M'] = 1000
        roman_d['0'] = 0
        
        s += '0'
        ans = 0
        for i in range(len(s)-1):
            if roman_d[s[i]] < roman_d[s[i+1]]:
                ans += roman_d[s[i]] * -1
            else:   
                ans += roman_d[s[i]]
            
        return ans   
        
   