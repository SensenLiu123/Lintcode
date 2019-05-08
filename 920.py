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
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        meetings = []
        for interval in intervals:
            meetings.append ( (interval.start, 1) )
            meetings.append( (interval.end, -1 ) )
            
        ongoing = 0
        
        for _, delta in sorted(meetings):
            ongoing += delta 
            
            if ongoing > 1:
                return False 
                
        return True 
        
