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
class Interval():
    def __int__(self, start, end):
        self.start = start
        self.end = end 

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        events = []
        for time in seqA:
            events.append((time.start, 1))
            events.append((time.end, -1 ))
            
        for time in seqB:
            events.append((time.start, 1))
            events.append((time.end, -1 ))
            
        ongoing = 0 
        switch = 0 
        ans = []
        
        for t, delta in sorted(events):
            ongoing += delta 
            
            if ongoing == 2 and switch == 0:
                intersection = Interval(t, t)
                switch = 1 - switch 
                continue
            if ongoing != 2 and switch == 1:
                intersection.end = t 
                ans.append(intersection)
                switch = 1 - switch
                continue 
            
        return ans 
            
            