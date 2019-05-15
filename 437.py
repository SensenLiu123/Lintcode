#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:05:55 2019

@author: sensenliu
"""

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages :
            return 0 
            
        start = max(pages)
        end = sum(pages)    
            
        if k > len(pages):
            return start

        if k == 1:
            return end  
            
        while start + 1 < end :
            mid = (start + end) // 2 
            
            if self.count_person(pages, mid) > k :
                start = mid 
            
            else:
                end = mid 
                
        if self.count_person(pages, start) > k:
            return end 
        
        return start 
                
        
    def count_person(self, pages, time_limit) :
        count = 1  
        indiv_time = 0 
        
        for book in pages:
            
            if indiv_time + book > time_limit:
                indiv_time = 0 
                count += 1 
            
            indiv_time += book 
                
        return count 
            
            
