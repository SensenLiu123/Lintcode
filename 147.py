#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # table = [[],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[],[153, 370, 371, 407],[1634, 8208, 9474],[54748, 92727, 93084], [548834],  [1741725, 4210818, 9800817, 9926315],[24678050, 24678051, 88593477]]
        
        # return table [n]
        
        
        if n == 0:
            return []
            
        low = int('1' + '0' * (n-1))
        high = int('9' * n)
        
        if n == 1:
            res = [0]
        else:
            res = []
        for num in range(low, high + 1):
            if not self.narci(num, n):
                continue 
            res.append(num)
            
        return res 
        
    def narci(self, num, n):
        narci_num = 0
        origin = num 
        while num > 0:
            digit = num % 10 
            narci_num += digit ** n 
            num //=10 
            
        return narci_num == origin 