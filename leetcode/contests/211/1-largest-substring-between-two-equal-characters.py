class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i]
            else:
                d[c].append(i)
                
        m = -1
        for v in d.values():
            v.sort()
            m = max(m, v[-1] - v[0] - 1)
            
        return m
