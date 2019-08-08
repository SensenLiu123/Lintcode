#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # if len(s) == 0:
        #     return []
            
        res = []
        self.dfs(s, 0, [], res)
        
        return res 
        
    def dfs(self, s, start, path, res):
        
        if start >= len(s):
            res.append(path[:]);
            return 
        
        for i in range(1, 3):
            
            if start + i > len(s):
                break 
            
            path.append(s[start: start + i])
            print(start)
            print(path)
            
            self.dfs(s, start + i , path ,res) ;
            
            path.pop()
            
            
test = Solution(); 

example = "123";

print(test.splitString(example))
          