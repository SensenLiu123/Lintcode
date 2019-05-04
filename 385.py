#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class ArrayListManager:
    '''
     * @param n: You should generate an array list of n elements.
     * @return: The array list your just created.
    '''
    def create(self, n):
        # Write your code here
        array = [i for i in range(n)]
        return array
    
    
    '''
     * @param list: The list you need to clone
     * @return: A deep copyed array list from the given list
    '''
    def clone(self, array):
        # Write your code here
        array_copy = list(array)
        return array_copy
    
    
    '''
     * @param list: The array list to find the kth element
     * @param k: Find the kth element
     * @return: The kth element
    '''
    def get(self, array, k):
        # Write your code here
        return array[k]
    
    '''
     * @param list: The array list
     * @param k: Find the kth element, set it to val
     * @param val: Find the kth element, set it to val
    '''
    def set(self, array, k, val):
        array[k] = val 
        return array 
    
    
    '''
     * @param list: The array list to remove the kth element
     * @param k: Remove the kth element
    '''
    def remove(self, array, k):
        # write tour code here
        del array[k]

    '''
     * @param list: The array list.
     * @param val: Get the index of the first element that equals to val
     * @return: Return the index of that element
    '''
    def indexOf(self, array, val):
        if val not in set(array):
            return -1 
        else:
            return array.index(val)