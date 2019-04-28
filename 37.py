#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10 
            
        ans = 0 
        power =  100 
        for digit in digits:
            ans += digit * power
            power //= 10 
            
        return ans 
            
