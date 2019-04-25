#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""

class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def __init__(self):
        self.root_hash = {}
        self.email_to_name = {}
    
    def accountsMerge(self, accounts):        
        for ac in accounts:
            if len(ac) < 2:
                continue 
            
            name = ac[0]
            temp_root = ac[1]
            
            for email in ac[1:]:
                self.email_to_name[email] = [name] 
                
                if email not in self.root_hash:
                    self.root_hash[email] = temp_root
                else:
                    true_root = self.find(email)
                    self.union(temp_root, true_root)
        
        root_kid = {}
        
        for email in self.root_hash:
            root = self.find(email)
            if root in root_kid:
                root_kid[root].append(email)
            else:
                root_kid[root] = [email]
            
        ans = []
        for root in root_kid:
            ans.append( self.email_to_name[root] + sorted(root_kid[root]) )
            
        return ans 
                    
    def union(self, a, root):
        # a, b are strings
        root_a = self.find(a)
        # root_b = self.find(b)
        
        if root_a == root:
            return 
        self.root_hash[root_a] = root 
        
    def find(self, node):
        path = []
        
        while node != self.root_hash[node]:
            path.append(node)
            node = self.root_hash[node]
            
        root = node
        for node in path:
            self.root_hash[node] = root 
            
        return root 
        
            
mysolution = Solution()   
inn = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]                    
print( mysolution.accountsMerge(inn)   )
print(mysolution.root_hash)
