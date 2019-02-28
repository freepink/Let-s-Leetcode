class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)
        
        temp = list(set(nums))
        
        for i in range(2):
            if temp:
                temp.remove(max(temp))
        
            
        if temp:
            return max(temp)
        else:
            return max(nums)
            
            '''
            
            Runtime: 40 ms, faster than 61.76% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.2 MB, less than 5.88% of Python3 online submissions for Third Maximum Number.
            
            
            
            '''
