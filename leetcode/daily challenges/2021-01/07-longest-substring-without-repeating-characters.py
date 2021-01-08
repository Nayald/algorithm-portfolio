class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n = 1
        n_max = n
        i = 1
        single = [-1] * 256
        single[ord(s[0])] = 0
        while i < len(s):
            if single[ord(s[i])] < 0:
                single[ord(s[i])] = i
                n += 1
            else:
                n_max = max(n_max, n)
                n = 1
                new_i = single[ord(s[i])] + 1
                single = [-1] * 256
                single[ord(s[new_i])] = new_i
                i = new_i
            i += 1
            
        return max(n_max, n)
                