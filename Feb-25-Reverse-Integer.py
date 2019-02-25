class Solution:
    # def reverse(self, x: int) -> int:
    def reverse(self,x):
        result =int(str(abs(x))[::-1])
        if x >= 0:
            return result if result <= pow(2,31)-1 else 0
        if x < 0:
            return -result if -result >= -pow(2,31) else 0
