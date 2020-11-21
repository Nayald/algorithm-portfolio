from collections import deque

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        result = 0
        k = 0
        m = n // 10
        while m:
            m //= 10
            k += 1
            result += len(digits) ** k
        
        def helper(s):
            if not s:
                return 1
            
            result = 0
            for d in digits:
                if str(d) < s[0]:
                    result += len(digits) ** (len(s) - 1)
                if str(d) == s[0]:
                    result += helper(s[1:])

            return result
            
            
        return result + helper(str(n))