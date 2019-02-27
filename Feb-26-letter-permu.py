class Solution:
    # def letterCasePermutation(self, S: str) -> List[str]:
    def letterCasePermutation(self,S):
        result = [""]
        if S.isdigit():
            return [S]
        else:
            for s in S:
                if s.isalpha():
                    result = [word + i for word in result 
                          for i in [s.lower(),s.upper()]]
                else:
                    result = [word + s for word in result]
        return result
       
       '''
       
64 / 64 test cases passed.
Status: Accepted
Runtime: 72 ms
Memory Usage: 13.6 MB
       '''
