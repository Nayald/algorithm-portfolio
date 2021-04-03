class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                k = i + 1
                while k < j and s[k] == s[i]:
                    k += 1
                    
                i = k
                l = j - 1
                while l > i and s[l] == s[j]:
                    l -= 1
                    
                j = l
            else:
                break
                
        return j - i + 1