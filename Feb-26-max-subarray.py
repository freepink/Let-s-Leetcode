class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self,nums):
        max_so_far = max(nums)
        for i in range(len(nums)):
            max_ending = nums[i]
            if max_so_far < max_ending:
                max_so_far = max_ending
                
            for j in range(i+1,len(nums)):
                max_ending += nums[j]
                if max_so_far < max_ending:
                    max_so_far = max_ending
          
        return max_so_far
        
        '''
        Runtime: 13660 ms, faster than 5.41% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.6 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
        '''
