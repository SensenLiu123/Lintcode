class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """
    def nextGreaterElements(self, nums):
        # nums is circular so we need to arrays 
        flattened = nums + nums ;
        
        stack = []
        nextGreater = {}
        
        for i in range(len(flattened)):
            
            while stack and flattened [stack[-1] ] < flattened[i]:
                currentIdx = stack.pop() ;
                nextGreater[currentIdx] = i ;
                
            stack.append(i)
                
            
            
        res = [-1] * len(nums) ;
        for i in range(len(nums)):
            if i not in nextGreater:
                continue ;
                
            res[i] = flattened[nextGreater[i] ]
            
        return res 

        
