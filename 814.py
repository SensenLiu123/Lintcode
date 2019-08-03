#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: sensenliu
"""

class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, A, B):
        if A == B:
            return 0
        
        queue = collections.deque([A])
        visited = set([A])
        
        travel = 0 

        while queue:
            travel += 1 
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for neighbor in node.neighbors:
                    if neighbor == B:
                        return travel 
                        
                    if neighbor in visited:
                        continue 
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        return -1 
                    
                    
                
            