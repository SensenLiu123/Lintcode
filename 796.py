#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:07:37 2019

@author: sensenliu
"""

class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns 
    """
    def openLock(self, deadends, target):
        start = '0000'
            
        dead = set(deadends)
        if start in dead:
            return -1 
            
        neighbors = set(self.get_next_node(target))
        if neighbors & dead == neighbors:
            return -1 
            
        visited = set()
        step = 0 
        queue = collections.deque([start])
        
        while queue:
            step += 1 
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node == target:
                    return step -1 
                    
                visited.add(node)
            
                for next_node in self.get_next_node(node):
                    if next_node in dead or next_node in visited:
                        continue 
                    
                    queue.append(next_node)
                    visited.add(next_node)
                    
        return -1 
                    
        
    def get_next_node(self, string):
        all_next = []
        for i in range(4):
            left, mid, right = string[:i], string[i], string[i+1:]
            mid = int(mid)
            for mid in [(mid + 1)% 10, (mid - 1) % 10]:
                all_next.append(left+str(mid)+right)
            
        return all_next