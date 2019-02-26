class Solution:
    # def dominantIndex(self, nums: List[int]) -> int:
    def dominantIndex(self,nums):
        max_value = max(nums,default = 0)        
        
        while nums:
            index = nums.index(max_value)
            nums.remove(max_value)
       
            while nums:
                if max([i*2 for i in nums]) <= max_value:
                    return index
                else:
                    return -1
            else:
                return 0
             
             '''Runtime: 40 ms, faster than 76.31% of Python3 online submissions for Largest Number At Least Twice of Others.
Memory Usage: 13.3 MB, less than 6.82% of Python3 online submissions for Largest Number At Least Twice of Others.'''
