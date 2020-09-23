class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split()
        return len(tmp[-1]) if tmp else 0