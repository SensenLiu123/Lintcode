#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:26:31 2019

@author: sensenliu
"""

class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # write your code here

        if len(tokens) % 2 == 0:
            return 0 
            
        symbols = "+-*/"    
        
        stack = []
        for string in tokens:
            if string not in symbols:
                
                stack.append(int(string))
            else:
                
                num2 = stack.pop()
                num1 = stack.pop()
                
                res = self.calc(num1, num2, string)
                
                stack.append(res)
                
                
        return stack.pop()
            
        
    def calc(self, a, b, ope):
        if ope == '+':
            return a + b
            
        if ope == '-':
            return a - b
            
        if ope == '*':
            return a * b 
            
        else:
            return int (a * 1.0 / b)