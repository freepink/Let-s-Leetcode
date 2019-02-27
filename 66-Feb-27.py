class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = [str(i) for i in digits]
        final = str(int("".join(temp)) + 1)
        return [int(i) for i in final]
        
        '''
        Runtime: 40 ms, faster than 55.18% of Python3 online submissions for Plus One.
Memory Usage: 13.2 MB, less than 5.29% of Python3 online submissions for Plus One.
Next challenges:
        '''
