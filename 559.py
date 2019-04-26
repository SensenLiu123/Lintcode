#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
import heapq 
class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and 
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        node = self.root 
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            self.add_frequence(node.top10, frequency)

    def add_frequence(self, top10, frequency):
        heapq.heappush(top10, frequency)
        if len(top10) > 10:
            heapq.heappop(top10)
           
        top10.sort(reverse = True)
            
        # top10.append(frequency)
        # top10.sort(reverse = True)
        # if len(top10) > 10:
        #     top10 = top10[:10]
            
            
                    
            
            
                
        
       


