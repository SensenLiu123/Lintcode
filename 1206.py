class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    def nextGreaterElement(self, nums1, nums2):
        if len(nums1) == 0 or len(nums2) == 0:
            return []
            
            
        stack = []
        valueIdx = {}
        nextGreater = {}
        
        for i in range(len(nums2)):
            valueIdx[nums2[i]] = i
            
            while stack and nums2 [stack[-1]] < nums2[i]:
                index = stack.pop() ;
                nextGreater[index] = i ;
                
            stack.append(i)
            
            
        res = []
        for number in nums1:
            numberIdx = valueIdx[number] ;
            
            if numberIdx in nextGreater:
                res.append(nums2[nextGreater[numberIdx]])
            else:
                res.append(-1)
                
        return res 
