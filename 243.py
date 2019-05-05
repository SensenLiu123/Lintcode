#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:54:22 2019

@author: sensenliu
"""

class Solution:
    """
    @param: k: An integer
    @return: all amicable pairs
    """
    def amicablePair(self, k):
        if k < 284:
            return []
        
        from_wiki = [[220, 284], [1184, 1210], [2620, 2924], [5020, 5564], [6232, 6368], [10744, 10856], [12285, 14595], [17296, 18416], [63020, 76084], [66928, 66992], [67095, 71145], [69615, 87633],[79750, 88730], [100485, 124155],[122265, 139815]]
        
        for i in range(1, len(from_wiki)):
            if k < from_wiki[i][1]:
                return from_wiki[: i]
                
        return from_wiki + self.very_large(k)
        
        
        
    def very_large(self, k):    
        ans = []
        for num in range(139814, k + 1):
            possible = self.divisor_sum(num)
            
            # need condition possible < num, otherwise there are identical pairs 
            if self.divisor_sum(possible) == num and possible < num:
                ans.append([possible, num])
            
        return ans 
        
    def divisor_sum(self, num):
        my_sum = 1;
        
        i = 2
        while i * i <= num + 1:
            if num % i == 0:
                my_sum += i + num //i
                
            if i * i == num:
                my_sum -= i
                
            i += 1 
            
        return my_sum
                
            