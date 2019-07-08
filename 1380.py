#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        
        # in: list of strings 
        # out: list of sorted strings 
        # rule: sort based on content 
        # what we need, a function that can tell its a number 
        # a function return index of the first space 
        
        
        withInt = []
        withStr = []
        for log in logs:
            if log.split(' ')[-1].isdigit():
                withInt.append(log)
            else:
                withStr.append(log)
        
        return sorted(withStr, key = Solution.mykey) + withInt
    
    @staticmethod
    def mykey(x):
        pos = x.index(' ')
        return (x[pos+1:], x[:pos])
            