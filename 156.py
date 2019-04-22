#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        
        if not intervals: 
            return []
            
        ans = []
        new_interv = sorted(intervals, key = lambda x:x.start)
        
        
        prev = None
        for current in new_interv:
            
            if prev is None or prev.end < current.start:
                ans.append(current)
                prev = current 
                
            else:   
                prev.end = max(prev.end, current.end)
        
        return ans                
                
                