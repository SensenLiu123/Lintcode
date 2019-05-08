#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        events = []
        
        for meeting in intervals:
            events.append([meeting.start, 1])
            events.append([meeting.end, -1])
            
            
        events.sort()
        print(events)
        
        count = 0 
        room = 0
        
        for event in events:
            count += event[1]

            if room < count:
                room = count
            print(room)
                
        return room
    
    
    
trial = Solution()
intervals = [Interval(0,30),Interval(5, 10), Interval(15, 20)]

print(trial.minMeetingRooms(intervals))        
