class Solution:
    # def reverse(self, x: int) -> int:
    def reverse(self,x):
        result =int(str(abs(x))[::-1])
        if x >= 0:
            return result if result <= pow(2,31)-1 else 0
        if x < 0:
            return -result if -result >= -pow(2,31) else 0

      '''Runtime: 56 ms, faster than 60.66% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.3 MB, less than 5.71% of Python3 online submissions for Reverse Integer.'''

