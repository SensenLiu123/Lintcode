#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # input is a string of digits, can be emoty or null 
        # output is an int, 
        # decode: 12 -> ab or l 
        #       101 -> i a 
        #       134 -> m d
        # decode rules: each time we take 1 or 2 digits off the string 
        #           number of decoding based on prev result + prev-2 result  
        #          constraints are 1-digit cannot be  0 
        #       constraints 2, 2-digits cannot be 0a, or larger than 26!
        # if we at string(i-1), the result is dp(i)! 
        # now start from initial case: 
        # 
        
        
        if len(s) == 0 or not s:
            return  0 

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 
        # if s[0] != '0':
        #     dp[1] += dp[0]

        for i in range(1, n  + 1) :
            if s[i - 1] != '0':
                dp[i] += dp[i - 1] 
                
            if i >= 2 and 10 <= int (s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2] 
                
        return dp[n]
                
            
        
