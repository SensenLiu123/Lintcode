#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class School:
    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''
    # write your code here
    def __init__(self, ):
        self.name = ''

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''
    # write your code here
    def setName(self, string):
        self.name = string 
        
    def getName(self):
        return self.name  