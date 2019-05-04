#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Student:

    
    '''
     * Declare a constructor expect a name as a parameter.
    '''
    def __init__(self, name):
        self.name = name 
        self.score = 0
    
    '''
     * Declare a public method `getLevel` to get the level(char) of this student.
    '''
    def getLevel(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'