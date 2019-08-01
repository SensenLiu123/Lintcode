#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:02:51 2019

@author: sensenliu
"""

class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        
        length = set()
        wordIdx = {}
        
        for i, word in enumerate(a):
            
            length.add(len(word));
        
            wordIdx[word] = i;
        
        lengthInDesOrder =  sorted(length, reverse = True );
        
        ans = '';
        
        i = 0
        while i < len(s):
            
            match = False 
            
            for possibleLength in lengthInDesOrder:
                if i + possibleLength > len(s):
                    continue;
                    
                substring = s[i: i + possibleLength];
                
                if substring in wordIdx:
                    # replace! 
                    ans += b[ wordIdx[substring] ] ;
                    match = True;
                    i += possibleLength ;
                    
                    break;
                    
            if not match:        
                ans += s[i]
                i += 1  
                    
                    
        return ans 
        
        