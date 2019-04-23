#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

DIR = [(0,1), (1,0), (0, -1), (-1, 0)]
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class UFS:
    def __init__(self):
        self.root_hash = {}
        self.count = 0
        
    def find(self, position):
        # position is a tuple 
        root = self.root_hash[position]
        
        if root == position:
            return root 
        else:
            return self.find(root)
            
    def union(self, old, new):
        root_old = self.find(old)
        root_new = self.find(new)
        
        if root_old == root_new:
            return 
        
        self.root_hash[root_new] = root_old
        self.count -= 1 

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        
        ufs = UFS()
        
        visited = set()
        ans = []

        for pair in operators:
            (x, y) = pair.x, pair.y 
            
            if (x, y) in visited:
                ans.append(ufs.count)
                continue 
            
            ufs.root_hash[(x,y)] = (x,y)
            visited.add( (x,y) )
            ufs.count += 1 
            
            for dx, dy in DIR:
                xx, yy = x + dx, y + dy
                if (xx, yy) not in visited:
                    continue
                if xx>=n or xx < 0 or yy >= m or yy < 0:
                    continue 
                
                ufs.union((xx, yy), (x, y))
                
            ans.append(ufs.count)
            
        return ans 
                
                
