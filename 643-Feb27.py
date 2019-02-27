class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    def findMaxAverage(self,nums,k):
        if k == 1:
            return max(nums)
        
        temp= 0
        for i in range(k):
            temp += nums[i]
        cur = temp
        
        for i in range(len(nums)-k):
            temp += -nums[i]+ nums[i+k]
            if temp> cur:
                cur = temp
        return cur/k
        
          '''
    将分类讨论思想融合到解题中
    Runtime: 152 ms, faster than 92.28% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 15.3 MB, less than 6.25% of Python3 online submissions for Maximum Average Subarray I.
    
    '''
        
        
