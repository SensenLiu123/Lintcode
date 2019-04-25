#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class TrieNode:
    def __init__(self):
        self.has_char = {}
        self.is_word = False 
    
class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        
        for char in word:
            if char not in node.has_char:
                node.has_char[char] = TrieNode()
                
            node = node.has_char[char]
            
        node.is_word = True 
    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        if not word:
            return False 
            
        return self.dfs(self.root, word, 0)
        
        
    def dfs(self, node, word, index):
        # need this line if has_char[candidate] = None in recursion 
        # or root is None 
        if not node:
            return False 
        
        if index >= len(word):
            return node.is_word
            
        char  = word[index]
        
        if char =='.':
            for candidate in node.has_char:
                if self.dfs(node.has_char[candidate], word, index + 1):
                    return True 
                
        else:
            # return self.dfs(node.has_char[char], word, index + 1)
            # char maynot exist in the dict, use get
            return self.dfs(node.has_char.get(char), word, index + 1 )
        
        # need this line if word is null 
        return False 
            
        
        
