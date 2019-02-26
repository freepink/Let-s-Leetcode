class Solution:
    # def romanToInt(self, s: str) -> int:
    def romanToInt(self,s):
        roman_nums = {"M":1000,"D":500,
                      "C":100,"L":50,"X":10,"V":5,"I":1}
        result = 0
        
        for i in range(len(s)-1):
            if roman_nums[s[i]] >= roman_nums[s[i+1]]:
                result += roman_nums[s[i]]
            
            else:
                result -= roman_nums[s[i]]
                
        result += roman_nums[s[-1]]
            
        return result
        
      '''
      Runtime: 136 ms, faster than 56.67% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.5 MB, less than 5.05% of Python3 online submissions for Roman to Integer.

      '''
