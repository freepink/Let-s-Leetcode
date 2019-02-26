class Solution:
    # def numJewelsInStones(self, J: str, S: str) -> int:
    def numJewelsInStones(self,J,S):
        js_dict = {}
        count = 0
        for i in J:         
            if i in S:
                js_dict[i] = S.count(i)
        return sum([i for i in js_dict.values()])
        
        '''Runtime: 40 ms, faster than 78.99% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.1 MB, less than 5.25% of Python3 online submissions for Jewels and Stones.'''
