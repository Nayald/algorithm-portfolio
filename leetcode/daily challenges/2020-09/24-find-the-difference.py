class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        chars = [0] * 26
        for c in s:
            chars[ord(c) - ord("a")] += 1
            
        for c in t:
            chars[ord(c) - ord("a")] -= 1
            
        return chr(ord("a") + chars.index(-1))
