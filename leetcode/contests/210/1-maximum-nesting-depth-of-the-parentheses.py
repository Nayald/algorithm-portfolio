class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = count = 0
        for c in s:
            if c == "(":
                count += 1
                if count > max_count:
                    max_count = count
            elif c == ")":
                count -= 1
                
        return max_count