from itertools import chain

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def helper(s, i=0):
            result = [s]
            for j in range(i, len(s)):
                if "a" <= s[j] <= "z":
                    result.extend(helper(s[:j] + s[j].upper() + s[j+1:], j + 1))
                elif "A" <= s[j] <= "Z":
                    result.extend(helper(s[:j] + s[j].lower() + s[j+1:], j + 1))
                    
            return result
            
        return helper(S)