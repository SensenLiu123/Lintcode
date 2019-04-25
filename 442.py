#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class TrieNode():
    def __init__(self):
        self.char_dict = {}
        self.is_word = False 

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for char in word:
            
            if char not in node.char_dict:
                node.char_dict[char] = TrieNode()
            
            node = node.char_dict[char]    
            
        node.is_word = True   
        
        
    def find(self, string):
        # find a string node, return None if it doesnt exist 
        node = self.root 
        for char in string:
            node = node.char_dict.get(char)
            
            if node is None:
                return None
                
        return node

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        
        node =  self.find(word) 
        
        return node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        
        return self.find(prefix) is not None 
