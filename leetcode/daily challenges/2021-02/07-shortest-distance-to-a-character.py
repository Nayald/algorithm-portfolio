class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [0] * len(s)
        dist = len(s)
        for i in range(len(s)):
            if s[i] == c:
                result[i] = dist = 0
            else:
                dist += 1
                result[i] = dist
                
        dist = len(s)
        for i in reversed(range(len(s))):
            if s[i] == c:
                result[i] = dist = 0
            else:
                dist += 1
                result[i] = min(result[i], dist)
                
        return result
                
        