#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        if "" in wordDict:
            wordDict.remove("")
        
        if len(wordDict) == 0:
            return []
            
        if len(s) == 0:
            return []
            
        
            
            
        memo = {}
        return self.memoi(s, wordDict, memo)
        
        
        
    def memoi(self, s, wordDict, memo):
        
        if s in memo:
            return memo[s]
            
            
        if not s:
            return []
            
        path = []
        
        if s in wordDict:
            path.append(s)
        
        for i in range(len(s)):
            
            if s[:i] in wordDict:
                substring = s[:i]
                
                for combination in self.memoi(s[i:], wordDict, memo):
                    path.append(substring + ' ' + combination)
                    
        memo[s] = path
        return path
        
        
        
            
        