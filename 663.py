#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:40:05 2019

@author: sensenliu
"""
import collections
EMP = 2147483647 
MOVES = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        
        m,n = len(rooms), len(rooms[0])
        
        queue = collections.deque()
        distance = {}
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                    distance[(i, j)] = 0
        
        #distance = -1            
        while queue:
            #distance += 1
            size = len(queue)
            for _ in range(size):
                x,y = queue.popleft()
                rooms[x][y] = distance[(x, y)] 
                
                for dx,dy in MOVES:
                    xx,yy = x+ dx, y+ dy
                    if (xx, yy) in distance:
                        continue 
                    if self.in_map_and_empty(rooms, xx, yy):
                        queue.append((xx,yy))
                        # rooms[xx][yy] = rooms[x][y] + 1
                        distance[(xx, yy)] = distance[(x, y)] + 1 

        return rooms
        
    def in_map_and_empty(self, rooms, x, y):
        m,n = len(rooms), len(rooms[0])
        return 0 <= x < m and 0 <= y < n and rooms[x][y] == EMP
    
                    
test = Solution();
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]] ;
test.wallsAndGates(rooms)     
        