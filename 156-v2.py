#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:04:53 2019

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
        # in: interval is a class not a List array?
        # interval start/end values can be negative ?
        # interval end values >= start 
        # But has to be int type right? No double, Long 
        # List can be empty?
        # the interval wont be empty or null? 
        # out: List of merged intervals 
        # ========================================================
        # merge: [1,2] and [2,3] => [1, 3] 
        # merge: [1, 2] and [4, 5] => the same 
        # merge: [1, 10] and [5,6] => [1, 10] 
        # so merge is comparision of prev end value and current start value. 
        # so we have a running prev_end, if current_start > prev_end, ans add current 
        # if not, update the prev interval end value 
        
        if len(intervals) <= 1:
            return intervals 
            
        ans = []
        
        intervals.sort(key = lambda x: x.start) 
        
        prev_end = - 2 ** 31 # integer 
        
        for current in intervals:
            if len(ans) == 0 or current.start > prev_end:
                ans.append(current) 
                prev_end = current.end 

            else: # merge , we update end point of the tail interval 
                prev_end = max(prev_end, current.end)
                ans[-1].end = prev_end
            
        return ans 
                
                
