#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, string):
        ans = {} 
        
        for char in string:
            ans[char] = ans.get(char, 0) + 1 ;
            
        return ans 