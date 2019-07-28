#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 23:32:30 2019

@author: sensenliu
"""
import collections 
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    
    def canFinish(self, numCourses, prerequisites):
        
        edges, degrees = self.getInDegree(prerequisites, numCourses) ; 
        
        starter = []
        for course in degrees:
            if degrees[course] == 0:
                starter.append(course)
        
        if len(starter) == 0:
            return False 
            
        queue = collections.deque(starter) ; 
        takeCount = 0 ; 
        
        while queue:
            node = queue.popleft() ; 
            takeCount += 1  ; 
            
            for following in edges[node]:
                degrees[following] -= 1 ;
                
                if degrees[following] == 0 :
                    queue.append(following) ; 
                    
                    
        return takeCount == numCourses            
                    
            

        
        
    def getInDegree(self, prerequisites, N):
        
        courseInDeg = {x: 0 for x in range(N)}
        courseUnlock = {x: [] for x in range(N)}
        
        for pair in prerequisites:
            
            later = pair[0]
            before = pair[1]
            
            courseInDeg[later] += 1 ;
            courseUnlock[before].append(later) ;
            
        return courseUnlock, courseInDeg ;



test = Solution();
N =  4 ; 
testIn = [[1,0],[2,1], [3,1]] ; 
print(test.canFinish(N,testIn))