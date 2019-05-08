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
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        events = []
        for interval in airplanes:
            # start event is 1 end is -1 
            # so that after sorting, end comes before start if time point same
            events.append([interval.start, 1])
            events.append([interval.end, -1])
            
        events.sort()
        
        count = 0 
        
        max_flight = 0
        
        for event in events:
            count += event[1]
                
            if count > max_flight:
                max_flight = count 
                
        return max_flight
                
        
                
        
        
