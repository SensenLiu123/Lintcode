#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param: a: parameter of the equation
    @param: b: parameter of the equation
    @param: c: parameter of the equation
    @return: a double array, contains at most two root
    """
    def rootOfEquation(self, a, b, c):
        if a == 0:
            return [-c * 1.0 / b]
        
        delta = b * b - 4.0 * a * c
        if delta < 0:
            return []
        
        if delta == 0:
            return [-b / (2.0 * a)]
        
        if a >= 0:
            return [(-b - math.sqrt(delta))/(2 * a),  (-b + math.sqrt(delta))/(2 * a)]
        else:
            return [(-b + math.sqrt(delta))/(2 * a),  (-b - math.sqrt(delta))/(2 * a)]
