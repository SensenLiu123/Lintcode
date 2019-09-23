class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        
        count = 0 
        if len(s) == 0 or len(s) == 1:
            
            return count 
            
            
        left, right = 0, len(s) - 1 
        
        while left < right:
            letter1, letter2 = s[left], s[right]
            
            count += self.getDist(letter1, letter2)
            
            left += 1 
            right -= 1 
            
            
        return count 
        
        
        
    def getDist(self, char1, char2):
        a, b = ord(char1), ord(char2)
        
        return abs(a-b)
            
            
