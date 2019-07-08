#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

import heapq # Priority Queue moduel 
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # input: List<String>, int 
        # out: List <String>
        # all solutions, sorted order 
        
        # count number of occurance 
        # use a min PQ of size k 
        # 难点在于 基于频率比较之后，word 比较和频率相反。
        # 当频率一样，让 word 靠前的入堆
        # sort 中当频率一样， 让word 考前当在后面！
        
        if not words or k == 0:
            return []
            
        word_occur = {}
        for string in words:
            word_occur[string] = word_occur.get(string, 0) + 1  
            
        pri_queue = []
        
        for word, occurance in word_occur.items():
            item = Pair(occurance, word)
            if len(pri_queue) < k:
                heapq.heappush(pri_queue, item)
            
            else:
                if item > pri_queue[0]:
                    heapq.heappop(pri_queue)
                    heapq.heappush(pri_queue, item )
                
        sort_pair = sorted(pri_queue) 
        
        ans = []
        for i in range(len(sort_pair) - 1, -1, -1) :
            ans.append(sort_pair[i].string)
            
        return ans 
        
class Pair:
    def __init__(self, count, string):
        self.count = count 
        self.string = string 
        
    def __eq__(self, other):
        return self.count == other.count and self.string == other.string 
        
    def __lt__(self, other) :
        if self.count == other.count :
            return self.string > other.string  
        else:
            return self.count < other.count 
            
    def __gt__ (self, other):
        if self.count == other.count:
            return self.string < other.string 
        else:
            return self.count > other.count 
            