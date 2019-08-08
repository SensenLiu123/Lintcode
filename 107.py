#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dic):
        
        k = len(s) 
        
        if k == 0:
            return True 
            
        if len(dic) == 0:
            return len(s) == 0
            
        maxLength = max(len(word) for word in dic)    
         
        if s in dic:
            return True 
            
            
        dp = [False] * (k+ 1)
        
        dp[0] = True 
        
        for i in range(k):
            for j in range(i + 1 , i + maxLength + 1 ):
                if j >= k + 1:
                    break ;
                
                if dp[i] == False:
                    continue
                
        
                if s[i: j] in dic:
                    dp[j] = True 
                    
                print(dp)
                    
                    
        return dp[-1]
    
    
    
test  =  Solution()
s = "aaaaaaa"
dic = set(["aaaa","aaa"])

print(test.wordBreak(s, dic))